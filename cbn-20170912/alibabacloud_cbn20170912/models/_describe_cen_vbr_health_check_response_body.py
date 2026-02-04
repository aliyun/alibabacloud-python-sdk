# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenVbrHealthCheckResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vbr_health_checks: main_models.DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The health check configuration of the VBR.
        self.vbr_health_checks = vbr_health_checks

    def validate(self):
        if self.vbr_health_checks:
            self.vbr_health_checks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vbr_health_checks is not None:
            result['VbrHealthChecks'] = self.vbr_health_checks.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VbrHealthChecks') is not None:
            temp_model = main_models.DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks()
            self.vbr_health_checks = temp_model.from_map(m.get('VbrHealthChecks'))

        return self

class DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks(DaraModel):
    def __init__(
        self,
        vbr_health_check: List[main_models.DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck] = None,
    ):
        self.vbr_health_check = vbr_health_check

    def validate(self):
        if self.vbr_health_check:
            for v1 in self.vbr_health_check:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VbrHealthCheck'] = []
        if self.vbr_health_check is not None:
            for k1 in self.vbr_health_check:
                result['VbrHealthCheck'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vbr_health_check = []
        if m.get('VbrHealthCheck') is not None:
            for k1 in m.get('VbrHealthCheck'):
                temp_model = main_models.DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck()
                self.vbr_health_check.append(temp_model.from_map(k1))

        return self

class DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        description: str = None,
        health_check_interval: int = None,
        health_check_only: bool = None,
        health_check_source_ip: str = None,
        health_check_target_ip: str = None,
        healthy_threshold: int = None,
        vbr_instance_id: str = None,
        vbr_instance_region_id: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The description.
        self.description = description
        # The time interval at which probe packets are sent during the health check. Unit: seconds.
        self.health_check_interval = health_check_interval
        # Indicates whether probing is enabled. Valid values:
        # 
        # *   **true**: Probing is enabled.
        # 
        #         If you enable probing, the system does not switch to another route if the detected route is not reachable.
        # 
        # *   **false**: Probing is disabled.
        # 
        #           If probing is disabled and a redundant route is specified, the system switches to the redundant route when the detected route is not reachable.
        self.health_check_only = health_check_only
        # The source IP address of the health check.
        self.health_check_source_ip = health_check_source_ip
        # The destination IP address of the health check.
        self.health_check_target_ip = health_check_target_ip
        # The number of probe packets that are sent during the health check.
        self.healthy_threshold = healthy_threshold
        # The VBR ID.
        self.vbr_instance_id = vbr_instance_id
        # The ID of the region where the VBR is deployed.
        self.vbr_instance_region_id = vbr_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.description is not None:
            result['Description'] = self.description

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_only is not None:
            result['HealthCheckOnly'] = self.health_check_only

        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip

        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id

        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckOnly') is not None:
            self.health_check_only = m.get('HealthCheckOnly')

        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')

        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')

        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')

        return self

