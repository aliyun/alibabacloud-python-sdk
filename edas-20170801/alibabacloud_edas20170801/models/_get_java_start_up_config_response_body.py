# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetJavaStartUpConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        java_start_up_config: main_models.GetJavaStartUpConfigResponseBodyJavaStartUpConfig = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The configuration of Java startup parameters.
        self.java_start_up_config = java_start_up_config
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.java_start_up_config:
            self.java_start_up_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.java_start_up_config is not None:
            result['JavaStartUpConfig'] = self.java_start_up_config.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('JavaStartUpConfig') is not None:
            temp_model = main_models.GetJavaStartUpConfigResponseBodyJavaStartUpConfig()
            self.java_start_up_config = temp_model.from_map(m.get('JavaStartUpConfig'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetJavaStartUpConfigResponseBodyJavaStartUpConfig(DaraModel):
    def __init__(
        self,
        original_configs: str = None,
        start_up_args: str = None,
    ):
        # The displayed startup parameter configuration.
        self.original_configs = original_configs
        # The effective startup parameter configuration.
        self.start_up_args = start_up_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.original_configs is not None:
            result['OriginalConfigs'] = self.original_configs

        if self.start_up_args is not None:
            result['StartUpArgs'] = self.start_up_args

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalConfigs') is not None:
            self.original_configs = m.get('OriginalConfigs')

        if m.get('StartUpArgs') is not None:
            self.start_up_args = m.get('StartUpArgs')

        return self

