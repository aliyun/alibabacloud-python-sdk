# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeActiveOperationMaintenanceConfigResponseBody(DaraModel):
    def __init__(
        self,
        config: main_models.DescribeActiveOperationMaintenanceConfigResponseBodyConfig = None,
        has_config: int = None,
        request_id: str = None,
    ):
        # The configuration details of the O&M task.
        self.config = config
        # Indicates whether the configuration exists. Valid values:
        # 
        # - 1: Configured.
        # - 0: Not configured.
        self.has_config = has_config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.has_config is not None:
            result['HasConfig'] = self.has_config

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.DescribeActiveOperationMaintenanceConfigResponseBodyConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('HasConfig') is not None:
            self.has_config = m.get('HasConfig')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeActiveOperationMaintenanceConfigResponseBodyConfig(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        cycle_time: str = None,
        cycle_type: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        modified_time: str = None,
        status: int = None,
    ):
        # The time when the O&M task configuration was created. The time is in the <i>yyyy-mm-dd</i>T<i>hh:mm:ss</i>Z format (UTC).
        self.created_time = created_time
        # The cycle time.
        # 
        # - If CycleType is set to Month, a number from 1 to 28 is returned, indicating the day of the month. Multiple values are separated by commas (,). The value is 0 if the configuration is inactive.
        # - If CycleType is set to Week, a number from 1 to 7 is returned, indicating the day of the week. Multiple values are separated by commas (,). The value is 0 if the configuration is inactive.
        self.cycle_time = cycle_time
        # The cycle type. Valid values:
        # 
        # - Month: monthly
        # - Week: weekly
        self.cycle_type = cycle_type
        # The end time of the O&M time window. The time is in the <i>hh:mm:ss</i>Z format (UTC).
        self.maintain_end_time = maintain_end_time
        # The start time of the O&M time window. The time is in the <i>hh:mm:ss</i>Z format (UTC).
        self.maintain_start_time = maintain_start_time
        # The time when the O&M task configuration was last modified. The time is in the <i>yyyy-mm-dd</i>T<i>hh:mm:ss</i>Z format (UTC).
        self.modified_time = modified_time
        # Indicates whether the configuration is active. Valid values:
        # 
        # - 1: Active.
        # - 2: Inactive.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.cycle_time is not None:
            result['CycleTime'] = self.cycle_time

        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CycleTime') is not None:
            self.cycle_time = m.get('CycleTime')

        if m.get('CycleType') is not None:
            self.cycle_type = m.get('CycleType')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

