# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeEnvCustomJobResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeEnvCustomJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeEnvCustomJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnvCustomJobResponseBodyData(DaraModel):
    def __init__(
        self,
        config_yaml: str = None,
        custom_job_name: str = None,
        environment_id: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # If the **encryptYaml** parameter is set to `true`, a Base64-encoded YAML string is returned. Otherwise, a plaintext YAML string is returned.
        self.config_yaml = config_yaml
        # The name of the custom job.
        self.custom_job_name = custom_job_name
        # The ID of the environment instance.
        self.environment_id = environment_id
        # The region ID.
        self.region_id = region_id
        # The status. Valid values:
        # 
        # *   run
        # *   stop
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_yaml is not None:
            result['ConfigYaml'] = self.config_yaml

        if self.custom_job_name is not None:
            result['CustomJobName'] = self.custom_job_name

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigYaml') is not None:
            self.config_yaml = m.get('ConfigYaml')

        if m.get('CustomJobName') is not None:
            self.custom_job_name = m.get('CustomJobName')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

