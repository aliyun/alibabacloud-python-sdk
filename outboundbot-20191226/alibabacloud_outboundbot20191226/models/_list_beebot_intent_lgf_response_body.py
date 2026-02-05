# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListBeebotIntentLgfResponseBody(DaraModel):
    def __init__(
        self,
        beebot_request_id: str = None,
        code: str = None,
        http_status_code: int = None,
        lgfs: List[main_models.ListBeebotIntentLgfResponseBodyLgfs] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.beebot_request_id = beebot_request_id
        self.code = code
        self.http_status_code = http_status_code
        self.lgfs = lgfs
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.lgfs:
            for v1 in self.lgfs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.beebot_request_id is not None:
            result['BeebotRequestId'] = self.beebot_request_id

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Lgfs'] = []
        if self.lgfs is not None:
            for k1 in self.lgfs:
                result['Lgfs'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeebotRequestId') is not None:
            self.beebot_request_id = m.get('BeebotRequestId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.lgfs = []
        if m.get('Lgfs') is not None:
            for k1 in m.get('Lgfs'):
                temp_model = main_models.ListBeebotIntentLgfResponseBodyLgfs()
                self.lgfs.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBeebotIntentLgfResponseBodyLgfs(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        intent_id: int = None,
        lgf_id: int = None,
        modify_time: str = None,
        rule_text: str = None,
    ):
        self.create_time = create_time
        self.intent_id = intent_id
        self.lgf_id = lgf_id
        self.modify_time = modify_time
        self.rule_text = rule_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.rule_text is not None:
            result['RuleText'] = self.rule_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RuleText') is not None:
            self.rule_text = m.get('RuleText')

        return self

