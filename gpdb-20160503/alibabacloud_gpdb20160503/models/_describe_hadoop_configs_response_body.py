# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHadoopConfigsResponseBody(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        config_value: str = None,
        request_id: str = None,
    ):
        # The name of the configuration file. Valid values:
        # 
        # *   hdfs-site
        # *   core-site
        # *   yarn-site
        # *   mapred-site
        # *   hive-site
        self.config_name = config_name
        # The configuration value.
        self.config_value = config_value
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

