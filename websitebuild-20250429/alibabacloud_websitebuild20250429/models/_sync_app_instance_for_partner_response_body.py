# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class SyncAppInstanceForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SyncAppInstanceForPartnerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
            temp_model = main_models.SyncAppInstanceForPartnerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SyncAppInstanceForPartnerResponseBodyData(DaraModel):
    def __init__(
        self,
        app_instance: main_models.SyncAppInstanceForPartnerResponseBodyDataAppInstance = None,
    ):
        self.app_instance = app_instance

    def validate(self):
        if self.app_instance:
            self.app_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance is not None:
            result['AppInstance'] = self.app_instance.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstance') is not None:
            temp_model = main_models.SyncAppInstanceForPartnerResponseBodyDataAppInstance()
            self.app_instance = temp_model.from_map(m.get('AppInstance'))

        return self

class SyncAppInstanceForPartnerResponseBodyDataAppInstance(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        return self

