# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApiMcpServerValidateHclRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
    ):
        # The content of the Terraform HCL code. For more information, see [HCL language overview](https://www.alibabacloud.com/help/en/terraform/terraform-configuration-and-hcl-language-overview).
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        return self

