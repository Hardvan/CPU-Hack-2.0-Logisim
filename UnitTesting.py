import unittest
import InstructionTemplateGenerator


class TestCap(unittest.TestCase):

    def test1(self):
        text = "MOV #5, R3"
        result = InstructionTemplateGenerator.getInstructionTemplate(text)
        self.assertEqual(result, "002b")

    def test2(self):
        text = "ADD R2, R3, R7"
        result = InstructionTemplateGenerator.getInstructionTemplate(text)
        self.assertEqual(result, "c09f")

    def test3(self):
        text = "MOV #5, R0"
        result = InstructionTemplateGenerator.getInstructionTemplate(text)
        self.assertEqual(result, "0028")

    def test4(self):
        text = "MOV #4, R1"
        result = InstructionTemplateGenerator.getInstructionTemplate(text)
        self.assertEqual(result, "0021")

    def test5(self):
        text = "MOV #a, R2"
        result = InstructionTemplateGenerator.getInstructionTemplate(text)
        self.assertEqual(result, "0052")

    def test6(self):
        text = "ADD R0, R1, R3"
        result = InstructionTemplateGenerator.getInstructionTemplate(text)
        self.assertEqual(result, "c00b")

    def test7(self):
        text = "AND R3, R2, R4"
        result = InstructionTemplateGenerator.getInstructionTemplate(text)
        self.assertEqual(result, "c8d4")


if __name__ == "__main__":
    unittest.main()
