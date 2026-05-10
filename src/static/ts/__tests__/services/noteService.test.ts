import type { Note } from "@/types/app";
import type { ResponseWithData, ResponseWithRedirect } from "@/types/responses";

import noteService from "@/services/noteService";

import { mockNote } from "@tests/__mocks__/note.mock";

const mockGetAllResponse: ResponseWithData<Note[]> = {
  code: "200",
  message: "OK",
  data: [mockNote],
};

const mockRedirectResponse: ResponseWithRedirect = {
  code: "200",
  message: "OK",
  redirect_to: "/",
};

const mockFetchSuccess = (data: unknown): void => {
  global.fetch = jest.fn().mockResolvedValue({
    ok: true,
    json: async () => await Promise.resolve(data),
  });
};

const mockFetchError = (status: number): void => {
  global.fetch = jest.fn().mockResolvedValue({
    ok: false,
    status,
  });
};

const mockFetchNetworkError = (message = "Network error"): void => {
  global.fetch = jest.fn().mockRejectedValue(new Error(message));
};

describe("noteService", () => {
  describe("getAll", () => {
    describe("when the request succeeds", () => {
      it("should return the response data", async () => {
        mockFetchSuccess(mockGetAllResponse);

        const result = await noteService.getAll();

        expect(result).toEqual(mockGetAllResponse);
      });

      it("should call fetch with the correct URL", async () => {
        mockFetchSuccess(mockGetAllResponse);

        await noteService.getAll();

        expect(global.fetch).toHaveBeenCalledWith("/api/v1/notes/");
      });
    });

    describe("when the response is not ok", () => {
      it("should throw an error with the status code", async () => {
        mockFetchError(500);

        await expect(noteService.getAll()).rejects.toThrow(
          "HTTP error! status: 500"
        );
      });
    });

    describe("when a network error occurs", () => {
      it("should throw the network error", async () => {
        mockFetchNetworkError("Network error");

        await expect(noteService.getAll()).rejects.toThrow("Network error");
      });
    });
  });

  describe("create", () => {
    describe("when the request succeeds", () => {
      it("should return the response data", async () => {
        mockFetchSuccess(mockRedirectResponse);

        const result = await noteService.create("Test note");

        expect(result).toEqual(mockRedirectResponse);
      });

      it("should call fetch with the correct URL, method and body", async () => {
        mockFetchSuccess(mockRedirectResponse);

        await noteService.create("Test note");

        expect(global.fetch).toHaveBeenCalledWith("/api/v1/notes/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ content: "Test note" }),
        });
      });
    });

    describe("when the response is not ok", () => {
      it("should throw an error with the status code", async () => {
        mockFetchError(400);

        await expect(noteService.create("Test note")).rejects.toThrow(
          "HTTP error! status: 400"
        );
      });
    });

    describe("when a network error occurs", () => {
      it("should throw the network error", async () => {
        mockFetchNetworkError();

        await expect(noteService.create("Test note")).rejects.toThrow(
          "Network error"
        );
      });
    });
  });

  describe("delete", () => {
    describe("when the request succeeds", () => {
      it("should return the response data", async () => {
        mockFetchSuccess(mockRedirectResponse);

        const result = await noteService.delete(1);

        expect(result).toEqual(mockRedirectResponse);
      });

      it("should call fetch with the correct URL and method", async () => {
        mockFetchSuccess(mockRedirectResponse);

        await noteService.delete(1);

        expect(global.fetch).toHaveBeenCalledWith("/api/v1/notes//1", {
          method: "DELETE",
        });
      });
    });

    describe("when the response is not ok", () => {
      it("should throw an error with the status code", async () => {
        mockFetchError(404);

        await expect(noteService.delete(1)).rejects.toThrow(
          "HTTP error! status: 404"
        );
      });
    });

    describe("when a network error occurs", () => {
      it("should throw the network error", async () => {
        mockFetchNetworkError();

        await expect(noteService.delete(1)).rejects.toThrow("Network error");
      });
    });
  });

  describe("edit", () => {
    describe("when the request succeeds", () => {
      it("should return the response data", async () => {
        mockFetchSuccess(mockRedirectResponse);

        const result = await noteService.edit(1, "Updated content");

        expect(result).toEqual(mockRedirectResponse);
      });

      it("should call fetch with the correct URL, method and body", async () => {
        mockFetchSuccess(mockRedirectResponse);

        await noteService.edit(1, "Updated content");

        expect(global.fetch).toHaveBeenCalledWith("/api/v1/notes//1", {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ content: "Updated content" }),
        });
      });
    });

    describe("when the response is not ok", () => {
      it("should throw an error with the status code", async () => {
        mockFetchError(500);

        await expect(noteService.edit(1, "Updated content")).rejects.toThrow(
          "HTTP error! status: 500"
        );
      });
    });

    describe("when a network error occurs", () => {
      it("should throw the network error", async () => {
        mockFetchNetworkError();

        await expect(noteService.edit(1, "Updated content")).rejects.toThrow(
          "Network error"
        );
      });
    });
  });
});
