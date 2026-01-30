# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsStreamsNotifyUrlConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_streams_notify_config: main_models.DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig = None,
        request_id: str = None,
    ):
        self.live_streams_notify_config = live_streams_notify_config
        self.request_id = request_id

    def validate(self):
        if self.live_streams_notify_config:
            self.live_streams_notify_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_streams_notify_config is not None:
            result['LiveStreamsNotifyConfig'] = self.live_streams_notify_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveStreamsNotifyConfig') is not None:
            temp_model = main_models.DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig()
            self.live_streams_notify_config = temp_model.from_map(m.get('LiveStreamsNotifyConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_type: str = None,
        domain_name: str = None,
        notify_url: str = None,
    ):
        self.auth_key = auth_key
        self.auth_type = auth_type
        self.domain_name = domain_name
        self.notify_url = notify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        return self

