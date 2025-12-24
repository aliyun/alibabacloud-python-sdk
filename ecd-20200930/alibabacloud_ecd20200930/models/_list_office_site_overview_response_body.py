# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ListOfficeSiteOverviewResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        office_site_overview_results: List[main_models.ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults] = None,
        request_id: str = None,
    ):
        # The token that is used to start the next query. If this parameter is empty, all results are returned.
        self.next_token = next_token
        # The office network information.
        self.office_site_overview_results = office_site_overview_results
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.office_site_overview_results:
            for v1 in self.office_site_overview_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['OfficeSiteOverviewResults'] = []
        if self.office_site_overview_results is not None:
            for k1 in self.office_site_overview_results:
                result['OfficeSiteOverviewResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.office_site_overview_results = []
        if m.get('OfficeSiteOverviewResults') is not None:
            for k1 in m.get('OfficeSiteOverviewResults'):
                temp_model = main_models.ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults()
                self.office_site_overview_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults(DaraModel):
    def __init__(
        self,
        has_expired_eds_count: int = None,
        has_expired_eds_count_for_group: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_status: str = None,
        region_id: str = None,
        running_eds_count: int = None,
        running_eds_count_for_group: int = None,
        total_eds_count: int = None,
        total_eds_count_for_group: int = None,
        vpc_type: str = None,
        will_expired_eds_count: int = None,
        will_expired_eds_count_for_group: int = None,
    ):
        # The number of expired cloud computers in the office network.
        self.has_expired_eds_count = has_expired_eds_count
        # The number of expired cloud computers in the cloud computer pool.
        self.has_expired_eds_count_for_group = has_expired_eds_count_for_group
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # The office network status.
        # 
        # Default values:
        # 
        # *   CONFIGUSERFAILED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   REGISTERING
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   REGISTERED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NEEDCONFIGTRUST
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CONFIGUSERING
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CONFIGTRUSTFAILED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ERROR
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CONFIGTRUSTING
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NEEDCONFIGUSER
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.office_site_status = office_site_status
        # The ID of the region where the office network resides.
        self.region_id = region_id
        # The number of cloud computers that are running in the office network.
        self.running_eds_count = running_eds_count
        # The number of running cloud computers in the cloud computer pool.
        self.running_eds_count_for_group = running_eds_count_for_group
        # The total number of cloud computers in the office network.
        self.total_eds_count = total_eds_count
        # The total number of cloud computers in the cloud computer pool.
        self.total_eds_count_for_group = total_eds_count_for_group
        # The office network type and its suitable VPC type.
        # 
        # Valid values:
        # 
        # *   standard (default): standard, exclusive VPC
        # *   customized: custom, user VPC
        # *   basic: basic, shared VPC
        self.vpc_type = vpc_type
        # The number of cloud computers that are about to expire in the office network.
        self.will_expired_eds_count = will_expired_eds_count
        # The number of cloud computers that are about to expire in the cloud computer pool.
        self.will_expired_eds_count_for_group = will_expired_eds_count_for_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_expired_eds_count is not None:
            result['HasExpiredEdsCount'] = self.has_expired_eds_count

        if self.has_expired_eds_count_for_group is not None:
            result['HasExpiredEdsCountForGroup'] = self.has_expired_eds_count_for_group

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.office_site_status is not None:
            result['OfficeSiteStatus'] = self.office_site_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.running_eds_count is not None:
            result['RunningEdsCount'] = self.running_eds_count

        if self.running_eds_count_for_group is not None:
            result['RunningEdsCountForGroup'] = self.running_eds_count_for_group

        if self.total_eds_count is not None:
            result['TotalEdsCount'] = self.total_eds_count

        if self.total_eds_count_for_group is not None:
            result['TotalEdsCountForGroup'] = self.total_eds_count_for_group

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        if self.will_expired_eds_count is not None:
            result['WillExpiredEdsCount'] = self.will_expired_eds_count

        if self.will_expired_eds_count_for_group is not None:
            result['WillExpiredEdsCountForGroup'] = self.will_expired_eds_count_for_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasExpiredEdsCount') is not None:
            self.has_expired_eds_count = m.get('HasExpiredEdsCount')

        if m.get('HasExpiredEdsCountForGroup') is not None:
            self.has_expired_eds_count_for_group = m.get('HasExpiredEdsCountForGroup')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OfficeSiteStatus') is not None:
            self.office_site_status = m.get('OfficeSiteStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RunningEdsCount') is not None:
            self.running_eds_count = m.get('RunningEdsCount')

        if m.get('RunningEdsCountForGroup') is not None:
            self.running_eds_count_for_group = m.get('RunningEdsCountForGroup')

        if m.get('TotalEdsCount') is not None:
            self.total_eds_count = m.get('TotalEdsCount')

        if m.get('TotalEdsCountForGroup') is not None:
            self.total_eds_count_for_group = m.get('TotalEdsCountForGroup')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        if m.get('WillExpiredEdsCount') is not None:
            self.will_expired_eds_count = m.get('WillExpiredEdsCount')

        if m.get('WillExpiredEdsCountForGroup') is not None:
            self.will_expired_eds_count_for_group = m.get('WillExpiredEdsCountForGroup')

        return self

