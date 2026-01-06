# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GetSparkAppWebUiAddressResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSparkAppWebUiAddressResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
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
            temp_model = main_models.GetSparkAppWebUiAddressResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSparkAppWebUiAddressResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        dbcluster_id: str = None,
        expiration_time_in_millis: int = None,
        web_ui_address: str = None,
    ):
        # The Spark application ID.
        self.app_id = app_id
        # The database ID.
        self.dbcluster_id = dbcluster_id
        # The expiration time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expiration_time_in_millis = expiration_time_in_millis
        # The URL of the web UI for the Spark application.
        self.web_ui_address = web_ui_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.expiration_time_in_millis is not None:
            result['ExpirationTimeInMillis'] = self.expiration_time_in_millis

        if self.web_ui_address is not None:
            result['WebUiAddress'] = self.web_ui_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExpirationTimeInMillis') is not None:
            self.expiration_time_in_millis = m.get('ExpirationTimeInMillis')

        if m.get('WebUiAddress') is not None:
            self.web_ui_address = m.get('WebUiAddress')

        return self

