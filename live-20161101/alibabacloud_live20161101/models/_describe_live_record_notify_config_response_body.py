# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveRecordNotifyConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_record_notify_config: main_models.DescribeLiveRecordNotifyConfigResponseBodyLiveRecordNotifyConfig = None,
        request_id: str = None,
    ):
        # The configuration of callbacks for live stream recording.
        self.live_record_notify_config = live_record_notify_config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_record_notify_config:
            self.live_record_notify_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_record_notify_config is not None:
            result['LiveRecordNotifyConfig'] = self.live_record_notify_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveRecordNotifyConfig') is not None:
            temp_model = main_models.DescribeLiveRecordNotifyConfigResponseBodyLiveRecordNotifyConfig()
            self.live_record_notify_config = temp_model.from_map(m.get('LiveRecordNotifyConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveRecordNotifyConfigResponseBodyLiveRecordNotifyConfig(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        need_status_notify: bool = None,
        notify_auth_key: str = None,
        notify_req_auth: bool = None,
        notify_url: str = None,
        on_demand_url: str = None,
    ):
        # The main streaming domain.
        self.domain_name = domain_name
        # Indicates whether recording status callbacks are enabled. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.need_status_notify = need_status_notify
        self.notify_auth_key = notify_auth_key
        self.notify_req_auth = notify_req_auth
        # The recording callback URL.
        self.notify_url = notify_url
        # The callback URL for on-demand recording.
        self.on_demand_url = on_demand_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.need_status_notify is not None:
            result['NeedStatusNotify'] = self.need_status_notify

        if self.notify_auth_key is not None:
            result['NotifyAuthKey'] = self.notify_auth_key

        if self.notify_req_auth is not None:
            result['NotifyReqAuth'] = self.notify_req_auth

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.on_demand_url is not None:
            result['OnDemandUrl'] = self.on_demand_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('NeedStatusNotify') is not None:
            self.need_status_notify = m.get('NeedStatusNotify')

        if m.get('NotifyAuthKey') is not None:
            self.notify_auth_key = m.get('NotifyAuthKey')

        if m.get('NotifyReqAuth') is not None:
            self.notify_req_auth = m.get('NotifyReqAuth')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('OnDemandUrl') is not None:
            self.on_demand_url = m.get('OnDemandUrl')

        return self

