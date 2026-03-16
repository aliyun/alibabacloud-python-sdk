# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class QuerySyncStatusByAliUidResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QuerySyncStatusByAliUidResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QuerySyncStatusByAliUidResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySyncStatusByAliUidResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        corp_id: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        latest_begin_time: str = None,
        latest_end_time: str = None,
        latest_success_time: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.corp_id = corp_id
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.latest_begin_time = latest_begin_time
        self.latest_end_time = latest_end_time
        self.latest_success_time = latest_success_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.latest_begin_time is not None:
            result['LatestBeginTime'] = self.latest_begin_time

        if self.latest_end_time is not None:
            result['LatestEndTime'] = self.latest_end_time

        if self.latest_success_time is not None:
            result['LatestSuccessTime'] = self.latest_success_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LatestBeginTime') is not None:
            self.latest_begin_time = m.get('LatestBeginTime')

        if m.get('LatestEndTime') is not None:
            self.latest_end_time = m.get('LatestEndTime')

        if m.get('LatestSuccessTime') is not None:
            self.latest_success_time = m.get('LatestSuccessTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

