# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ExportApplicationConfigsResponseBody(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.ExportApplicationConfigsResponseBodyApplicationConfigs] = None,
        request_id: str = None,
    ):
        # The list of exported application configurations.
        self.application_configs = application_configs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application_configs:
            for v1 in self.application_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k1 in self.application_configs:
                result['ApplicationConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k1 in m.get('ApplicationConfigs'):
                temp_model = main_models.ExportApplicationConfigsResponseBodyApplicationConfigs()
                self.application_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ExportApplicationConfigsResponseBodyApplicationConfigs(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        config_file_name: str = None,
        content: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The file name.
        self.config_file_name = config_file_name
        # The file content. The content is Base64-encoded.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name

        if self.content is not None:
            result['Content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        return self

