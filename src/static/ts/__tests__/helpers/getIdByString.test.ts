import { getIdByString } from "@/helpers/getIdByString";

describe("getIdByString", () => {
  describe("with a single separator occurrence", () => {
    it("should return the part after the separator", () => {
      expect(getIdByString("note-123", "-")).toBe("123");
    });
  });

  describe("with multiple separator occurrences", () => {
    it("should return the last part", () => {
      expect(getIdByString("a-b-c-123", "-")).toBe("123");
    });
  });

  describe("when the separator is not present", () => {
    it("should return the full string", () => {
      expect(getIdByString("note123", "-")).toBe("note123");
    });
  });

  describe("with an empty string", () => {
    it("should return an empty string", () => {
      expect(getIdByString("", "-")).toBe("");
    });
  });

  describe("when the string ends with the separator", () => {
    it("should return an empty string", () => {
      expect(getIdByString("note-", "-")).toBe("");
    });
  });

  describe("when the string is only the separator", () => {
    it("should return an empty string", () => {
      expect(getIdByString("-", "-")).toBe("");
    });
  });

  describe("with a different separator", () => {
    it("should split by the given separator", () => {
      expect(getIdByString("note_123", "_")).toBe("123");
    });
  });
});
