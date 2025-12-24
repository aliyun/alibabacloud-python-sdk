# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveLazyPullStreamConfigResponseBody(DaraModel):
    def __init__(
        self,
        live_lazy_pull_config_list: main_models.DescribeLiveLazyPullStreamConfigResponseBodyLiveLazyPullConfigList = None,
        request_id: str = None,
    ):
        # The configurations of triggered stream pulling.
        self.live_lazy_pull_config_list = live_lazy_pull_config_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.live_lazy_pull_config_list:
            self.live_lazy_pull_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_lazy_pull_config_list is not None:
            result['LiveLazyPullConfigList'] = self.live_lazy_pull_config_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveLazyPullConfigList') is not None:
            temp_model = main_models.DescribeLiveLazyPullStreamConfigResponseBodyLiveLazyPullConfigList()
            self.live_lazy_pull_config_list = temp_model.from_map(m.get('LiveLazyPullConfigList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveLazyPullStreamConfigResponseBodyLiveLazyPullConfigList(DaraModel):
    def __init__(
        self,
        live_lazy_pull_config: List[main_models.DescribeLiveLazyPullStreamConfigResponseBodyLiveLazyPullConfigListLiveLazyPullConfig] = None,
    ):
        self.live_lazy_pull_config = live_lazy_pull_config

    def validate(self):
        if self.live_lazy_pull_config:
            for v1 in self.live_lazy_pull_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveLazyPullConfig'] = []
        if self.live_lazy_pull_config is not None:
            for k1 in self.live_lazy_pull_config:
                result['LiveLazyPullConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_lazy_pull_config = []
        if m.get('LiveLazyPullConfig') is not None:
            for k1 in m.get('LiveLazyPullConfig'):
                temp_model = main_models.DescribeLiveLazyPullStreamConfigResponseBodyLiveLazyPullConfigListLiveLazyPullConfig()
                self.live_lazy_pull_config.append(temp_model.from_map(k1))

        return self

class DescribeLiveLazyPullStreamConfigResponseBodyLiveLazyPullConfigListLiveLazyPullConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        pull_app_name: str = None,
        pull_args: str = None,
        pull_domain_name: str = None,
        pull_protocol: str = None,
        transcode_lazy: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The main streaming domain.
        self.domain_name = domain_name
        # The name of the application for back-to-origin stream pulling. If the application specified in the streaming URL is used, this parameter is left empty.
        self.pull_app_name = pull_app_name
        # The parameters of back-to-origin stream pulling.
        self.pull_args = pull_args
        # The domain name for back-to-origin stream pulling.
        self.pull_domain_name = pull_domain_name
        # The protocol for back-to-origin stream pulling. Valid values:
        # 
        # *   **rtmp**
        # *   **httpflv**
        # *   **hls**
        self.pull_protocol = pull_protocol
        # Indicates whether stream pulling is triggered when the transcoded stream is played. Default value: **no**. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.transcode_lazy = transcode_lazy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.pull_app_name is not None:
            result['PullAppName'] = self.pull_app_name

        if self.pull_args is not None:
            result['PullArgs'] = self.pull_args

        if self.pull_domain_name is not None:
            result['PullDomainName'] = self.pull_domain_name

        if self.pull_protocol is not None:
            result['PullProtocol'] = self.pull_protocol

        if self.transcode_lazy is not None:
            result['TranscodeLazy'] = self.transcode_lazy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PullAppName') is not None:
            self.pull_app_name = m.get('PullAppName')

        if m.get('PullArgs') is not None:
            self.pull_args = m.get('PullArgs')

        if m.get('PullDomainName') is not None:
            self.pull_domain_name = m.get('PullDomainName')

        if m.get('PullProtocol') is not None:
            self.pull_protocol = m.get('PullProtocol')

        if m.get('TranscodeLazy') is not None:
            self.transcode_lazy = m.get('TranscodeLazy')

        return self

