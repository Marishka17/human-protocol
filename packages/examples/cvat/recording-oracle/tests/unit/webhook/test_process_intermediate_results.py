from src.schemas.agreement import ImageLabelBinaryJobResults
from src.utils.process_intermediate_results import process_image_label_binary_intermediate_results


def test_process_image_label_binary_intermediate_results(intermediate_results):
    results = process_image_label_binary_intermediate_results(intermediate_results)
    assert ImageLabelBinaryJobResults.validate(results)
