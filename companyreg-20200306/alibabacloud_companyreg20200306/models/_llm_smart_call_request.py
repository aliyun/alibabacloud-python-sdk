# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LlmSmartCallRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        caller_number: str = None,
        product_code: str = None,
        prompt_param: str = None,
        scenes_code: str = None,
        skill_type: int = None,
        start_word_param: str = None,
        tenant_code: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.caller_number = caller_number
        self.product_code = product_code
        self.prompt_param = prompt_param
        self.scenes_code = scenes_code
        self.skill_type = skill_type
        self.start_word_param = start_word_param
        self.tenant_code = tenant_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.prompt_param is not None:
            result['PromptParam'] = self.prompt_param

        if self.scenes_code is not None:
            result['ScenesCode'] = self.scenes_code

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        if self.start_word_param is not None:
            result['StartWordParam'] = self.start_word_param

        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('PromptParam') is not None:
            self.prompt_param = m.get('PromptParam')

        if m.get('ScenesCode') is not None:
            self.scenes_code = m.get('ScenesCode')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        if m.get('StartWordParam') is not None:
            self.start_word_param = m.get('StartWordParam')

        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')

        return self

