# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCardSmsTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        factorys: str = None,
        memo: str = None,
        template_shrink: str = None,
        template_name: str = None,
    ):
        # The mobile phone manufacturer. Valid values:
        # 
        # *   **HuaWei**: HUAWEI
        # *   **XiaoMi**: Xiaomi
        # *   **OPPO**: OPPO
        # *   **VIVO**: vivo
        # *   **MEIZU**: MEIZU
        # 
        # > If this parameter is not specified, the system automatically specifies a supported mobile phone manufacturer.
        self.factorys = factorys
        # The description of the message template.
        self.memo = memo
        # The content of the card message template.
        # 
        # > 
        # 
        # *   For information about fields such as Template, ExtendInfo, TemplateContent, TmpCard, and Action, see [Parameters of card message templates](https://help.aliyun.com/document_detail/434929.html).
        # 
        # *   Message template content varies based on the template type. For more information, see [Sample message templates](https://help.aliyun.com/document_detail/435361.html).
        # 
        # This parameter is required.
        self.template_shrink = template_shrink
        # The name of the card message template.
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

        if self.template_shrink is not None:
            result['Template'] = self.template_shrink

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
            self.template_shrink = m.get('Template')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

