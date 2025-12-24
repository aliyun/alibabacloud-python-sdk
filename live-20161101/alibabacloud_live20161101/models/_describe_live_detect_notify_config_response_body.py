# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDetectNotifyConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_detect_notify_config: main_models.DescribeLiveDetectNotifyConfigResponseBodyLiveDetectNotifyConfig = None,
        request_id: str = None,
    ):
        # The callback configuration.
        self.live_detect_notify_config = live_detect_notify_config
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.live_detect_notify_config:
            self.live_detect_notify_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_detect_notify_config is not None:
            result['LiveDetectNotifyConfig'] = self.live_detect_notify_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveDetectNotifyConfig') is not None:
            temp_model = main_models.DescribeLiveDetectNotifyConfigResponseBodyLiveDetectNotifyConfig()
            self.live_detect_notify_config = temp_model.from_map(m.get('LiveDetectNotifyConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDetectNotifyConfigResponseBodyLiveDetectNotifyConfig(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        notify_url: str = None,
    ):
        # The main streaming domain.
        self.domain_name = domain_name
        # The callback URL.
        self.notify_url = notify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        return self

