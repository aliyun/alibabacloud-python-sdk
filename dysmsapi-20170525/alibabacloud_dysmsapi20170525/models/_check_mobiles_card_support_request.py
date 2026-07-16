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
        # The list of phone numbers to be queried.
        # 
        # This parameter is required.
        self.mobiles = mobiles
        # The code of the card SMS template.
        # Log on to the SMS Service console and go to the [Domestic Card SMS](https://dysms.console.aliyun.com/domestic/card) page. On the **Template Management** tab, you can view the list of card SMS templates.
        # 
        # >The template must be added and approved.
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

