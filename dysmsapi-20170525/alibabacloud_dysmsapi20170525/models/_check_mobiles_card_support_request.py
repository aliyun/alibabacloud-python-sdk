# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class CheckMobilesCardSupportRequest(DaraModel):
    def __init__(
        self,
        mobiles: List[Dict[str, Any]] = None,
        template_code: str = None,
    ):
        # The list of mobile phone numbers that receive messages.
        # 
        # This parameter is required.
        self.mobiles = mobiles
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

