# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateCardSmsTemplateRequest(DaraModel):
    def __init__(
        self,
        factorys: str = None,
        memo: str = None,
        template: Dict[str, Any] = None,
        template_name: str = None,
    ):
        # The vendors to which the template will be submitted. Valid values:
        # 
        # - **HuaWei**: Huawei
        # 
        # - **XiaoMi**: Xiaomi
        # 
        # - **OPPO**: OPPO
        # 
        # - **VIVO**: VIVO
        # 
        # - **MEIZU**: MEIZU
        # 
        # - **HONOR**: HONOR
        # 
        # > If you do not specify this parameter, the system automatically submits the template to all supported mobile phone vendors.
        self.factorys = factorys
        # A description of the template.
        self.memo = memo
        # The content of the card SMS template.
        # 
        # > - For more information about the `Template`, `ExtendInfo`, `TemplateContent`, `TmpCard`, and `Action` fields, see [Card SMS template parameters](https://help.aliyun.com/document_detail/434929.html).
        # >
        # > - The content structure varies based on the type of card SMS template. For more information, see [Card SMS template examples](https://help.aliyun.com/document_detail/435361.html).
        # 
        # This parameter is required.
        self.template = template
        # The name of the card SMS template.
        # 
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.factorys is not None:
            result['Factorys'] = self.factorys

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.template is not None:
            result['Template'] = self.template

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Factorys') is not None:
            self.factorys = m.get('Factorys')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

