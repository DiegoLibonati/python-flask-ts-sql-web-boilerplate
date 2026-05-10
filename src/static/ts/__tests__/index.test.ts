import { screen, waitFor } from "@testing-library/dom";
import userEvent from "@testing-library/user-event";

import noteService from "@/services/noteService";

import "@/index";

jest.mock("@/services/noteService", () => ({
  __esModule: true,
  default: {
    create: jest.fn(),
    delete: jest.fn(),
    edit: jest.fn(),
    getAll: jest.fn(),
  },
}));

const mockNoteService = jest.mocked(noteService);

const mockRedirectResponse = {
  code: "200",
  message: "OK",
  redirect_to: "/",
};

const buildDOMAndInit = (): void => {
  document.body.innerHTML = `
    <nav class="js-navbar"></nav>
    <button class="js-open-navbar header__action--active">Open navbar</button>
    <button class="js-close-navbar">Close navbar</button>
    <ul>
      <li id="alert-1" class="js-alert">Alert<button id="close-alert-1" class="js-close-alert">Close alert</button></li>
    </ul>
    <input class="js-input" />
    <button class="js-btn-add-note">Add note</button>
    <div id="note-1">
      <div>
        <div>
          <textarea class="js-text-area" disabled>Content</textarea>
          <button class="js-btn-edit-note">Edit</button>
          <button class="js-btn-confirm-edit-note">Confirm edit</button>
          <button class="js-btn-delete-note">Delete</button>
        </div>
      </div>
    </div>
  `;
  document.dispatchEvent(new Event("DOMContentLoaded"));
};

describe("index", () => {
  beforeEach(() => {
    buildDOMAndInit();
  });

  afterEach(() => {
    document.body.innerHTML = "";
  });

  describe("onClickCloseAlert", () => {
    it("should remove the alert when close button is clicked", async () => {
      const user = userEvent.setup();
      const alertEl = document.querySelector<HTMLLIElement>("#alert-1");

      expect(alertEl).toBeInTheDocument();

      await user.click(screen.getByRole("button", { name: "Close alert" }));

      expect(alertEl).not.toBeInTheDocument();
    });
  });

  describe("onClickOpenNavbar", () => {
    it("should open the navbar and update button states", async () => {
      const user = userEvent.setup();
      const openBtn = screen.getByRole("button", { name: "Open navbar" });
      const closeBtn = screen.getByRole("button", { name: "Close navbar" });
      const navbar = document.querySelector<HTMLElement>(".js-navbar");

      await user.click(openBtn);

      expect(openBtn).not.toHaveClass("header__action--active");
      expect(closeBtn).toHaveClass("header__action--active");
      expect(navbar).toHaveClass("nav--open");
    });
  });

  describe("onClickCloseNavbar", () => {
    it("should close the navbar and restore button states", async () => {
      const user = userEvent.setup();
      const openBtn = screen.getByRole("button", { name: "Open navbar" });
      const closeBtn = screen.getByRole("button", { name: "Close navbar" });
      const navbar = document.querySelector<HTMLElement>(".js-navbar");

      navbar?.classList.add("nav--open");
      closeBtn.classList.add("header__action--active");
      openBtn.classList.remove("header__action--active");

      await user.click(closeBtn);

      expect(closeBtn).not.toHaveClass("header__action--active");
      expect(openBtn).toHaveClass("header__action--active");
      expect(navbar).not.toHaveClass("nav--open");
    });
  });

  describe("onClickAddNote", () => {
    it("should call noteService.create with the input content", async () => {
      const user = userEvent.setup();
      mockNoteService.create.mockResolvedValue(mockRedirectResponse);

      const input = document.querySelector<HTMLInputElement>(".js-input")!;
      await user.type(input, "New note content");
      await user.click(screen.getByRole("button", { name: "Add note" }));

      await waitFor(() => {
        expect(mockNoteService.create).toHaveBeenCalledWith("New note content");
      });
    });

    it("should not call noteService.create when input is empty", async () => {
      const user = userEvent.setup();

      await user.click(screen.getByRole("button", { name: "Add note" }));

      expect(mockNoteService.create).not.toHaveBeenCalled();
    });

    it("should not call noteService.create when input has only whitespace", async () => {
      const user = userEvent.setup();

      const input = document.querySelector<HTMLInputElement>(".js-input")!;
      await user.type(input, "   ");
      await user.click(screen.getByRole("button", { name: "Add note" }));

      expect(mockNoteService.create).not.toHaveBeenCalled();
    });
  });

  describe("onClickEditNote", () => {
    it("should enable the textarea and toggle button visibility", async () => {
      const user = userEvent.setup();
      const textarea =
        document.querySelector<HTMLTextAreaElement>(".js-text-area")!;

      await user.click(screen.getByRole("button", { name: "Edit" }));

      expect(textarea).not.toHaveAttribute("disabled");
      expect(screen.getByRole("button", { name: "Edit" })).toHaveClass(
        "is-hidden"
      );
      expect(screen.getByRole("button", { name: "Confirm edit" })).toHaveClass(
        "is-visible"
      );
    });
  });

  describe("onClickConfirmEditNote", () => {
    it("should call noteService.edit with the note id and textarea content", async () => {
      const user = userEvent.setup();
      mockNoteService.edit.mockResolvedValue(mockRedirectResponse);

      const textarea =
        document.querySelector<HTMLTextAreaElement>(".js-text-area")!;
      textarea.value = "Updated content";

      await user.click(screen.getByRole("button", { name: "Confirm edit" }));

      await waitFor(() => {
        expect(mockNoteService.edit).toHaveBeenCalledWith(1, "Updated content");
      });
    });

    it("should disable the textarea and restore button states after click", async () => {
      const user = userEvent.setup();
      mockNoteService.edit.mockResolvedValue(mockRedirectResponse);

      const textarea =
        document.querySelector<HTMLTextAreaElement>(".js-text-area")!;
      textarea.value = "Some content";

      await user.click(screen.getByRole("button", { name: "Confirm edit" }));

      expect(textarea).toHaveAttribute("disabled");
      expect(
        screen.getByRole("button", { name: "Confirm edit" })
      ).not.toHaveClass("is-visible");
      expect(screen.getByRole("button", { name: "Edit" })).not.toHaveClass(
        "is-hidden"
      );
    });

    it("should not call noteService.edit when textarea content is empty", async () => {
      const user = userEvent.setup();

      const textarea =
        document.querySelector<HTMLTextAreaElement>(".js-text-area")!;
      textarea.value = "";

      await user.click(screen.getByRole("button", { name: "Confirm edit" }));

      expect(mockNoteService.edit).not.toHaveBeenCalled();
    });
  });

  describe("onClickDeleteNote", () => {
    it("should call noteService.delete with the note id", async () => {
      const user = userEvent.setup();
      mockNoteService.delete.mockResolvedValue(mockRedirectResponse);

      await user.click(screen.getByRole("button", { name: "Delete" }));

      await waitFor(() => {
        expect(mockNoteService.delete).toHaveBeenCalledWith(1);
      });
    });
  });
});
