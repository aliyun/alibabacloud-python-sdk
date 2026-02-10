# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class UpdateBaselineCheckWhiteRecordResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateBaselineCheckWhiteRecordResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.UpdateBaselineCheckWhiteRecordResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateBaselineCheckWhiteRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        lang: str = None,
        reason: str = None,
        record_id: int = None,
        source: str = None,
        target: str = None,
        target_type: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The reason why the check item is added to the whitelist.
        self.reason = reason
        # The ID of the whitelist record.
        self.record_id = record_id
        # The data source. Valid values:
        # 
        # *   **default**: server
        # *   **agentless**: agentless detection
        self.source = source
        # The object that is added to the whitelist.
        self.target = target
        # The type of the assets on which the whitelist rule takes effect. Valid values:
        # 
        # *   **all_instance**: all servers
        # *   **instance**: specific servers
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.source is not None:
            result['Source'] = self.source

        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

