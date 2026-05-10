import { getInputById } from "@/helpers/getInputById";

describe("getInputById", () => {
  afterEach(() => {
    document.body.innerHTML = "";
  });

  describe("when an input with the given id exists", () => {
    it("should return the matching input element", () => {
      const input = document.createElement("input");
      input.id = "input-1";
      input.className = "js-input";
      document.body.appendChild(input);

      expect(getInputById("input-1")).toBe(input);
    });
  });

  describe("when multiple inputs exist", () => {
    it("should return the input with the matching id", () => {
      const input1 = document.createElement("input");
      input1.id = "input-1";
      input1.className = "js-input";

      const input2 = document.createElement("input");
      input2.id = "input-2";
      input2.className = "js-input";

      document.body.appendChild(input1);
      document.body.appendChild(input2);

      expect(getInputById("input-2")).toBe(input2);
    });

    it("should not return an input with a non-matching id", () => {
      const input1 = document.createElement("input");
      input1.id = "input-1";
      input1.className = "js-input";

      const input2 = document.createElement("input");
      input2.id = "input-2";
      input2.className = "js-input";

      document.body.appendChild(input1);
      document.body.appendChild(input2);

      expect(getInputById("input-99")).toBeUndefined();
    });
  });

  describe("when no input with the given id exists", () => {
    it("should return undefined", () => {
      const input = document.createElement("input");
      input.id = "input-1";
      input.className = "js-input";
      document.body.appendChild(input);

      expect(getInputById("input-99")).toBeUndefined();
    });
  });

  describe("when no inputs exist in the DOM", () => {
    it("should return undefined", () => {
      expect(getInputById("input-1")).toBeUndefined();
    });
  });

  describe("when an input exists but has a different class", () => {
    it("should return undefined", () => {
      const input = document.createElement("input");
      input.id = "input-1";
      input.className = "other-class";
      document.body.appendChild(input);

      expect(getInputById("input-1")).toBeUndefined();
    });
  });
});
