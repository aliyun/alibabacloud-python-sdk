def test_green_20220302_imports_with_current_tea_openapi():
    from alibabacloud_green20220302 import models
    from alibabacloud_green20220302.client import Client

    assert models.TextModerationRequest is not None
    assert Client is not None
