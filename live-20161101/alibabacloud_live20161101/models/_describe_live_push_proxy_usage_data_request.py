# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLivePushProxyUsageDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        split_by: str = None,
        start_time: str = None,
    ):
        # The main streaming domain to query.
        # 
        # *   You can query one or more domain names. If you specify multiple domain names, separate them with commas (,).
        # *   If you leave this parameter empty, the data of all domain names within your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        self.owner_id = owner_id
        # The ID of the region. Separate multiple region IDs with commas (,). Valid values:
        # 
        # *   cn-beijing: China (Beijing)
        # *   cn-shanghai: China (Shanghai)
        # *   cn-shenzhen: China (Shenzhen)
        # *   cn-qingdao: China (Qingdao)
        # *   ap-southeast-1: Singapore
        # *   eu-central-1: Germany (Frankfurt)
        # *   ap-northeast-1: Japan (Tokyo)
        # *   ap-southeast-5: Indonesia (Jakarta)
        # 
        # If you do not specify this parameter, data of all regions is aggregated and returned by default.
        self.region = region
        self.region_id = region_id
        # The key that is used to group data. If you do not specify this parameter, the default value region is used. Data is aggregated and returned. Separate multiple keys with commas (,). Valid values:
        # 
        # *   domain: The value of DomainName in the response takes effect only if SplitBy is set to domain.
        # *   region: This is the default value. The value of Region in the response takes effect only if SplitBy is set to region.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. By default, data in the last seven days is returned.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.split_by is not None:
            result['SplitBy'] = self.split_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

