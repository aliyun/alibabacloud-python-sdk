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
        # The ingest domain name of the streamer to query.
        # - You can specify a single domain name or multiple domain names separated by commas (,).
        # - If this parameter is left empty, the aggregated data of all live streaming domain names is returned by default.
        self.domain_name = domain_name
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        self.owner_id = owner_id
        # The live center to query. You can specify multiple regions separated by commas (,). Valid values:
        # - cn-beijing: Beijing
        # - cn-shanghai: Shanghai
        # - cn-shenzhen: Shenzhen
        # - cn-qingdao: Qingdao
        # - ap-southeast-1: Singapore
        # - eu-central-1: Germany
        # - ap-northeast-1: Tokyo
        # - ap-southeast-5: Jakarta
        # 
        # If this parameter is left empty, the aggregated data of all regions is returned by default.
        self.region = region
        # The region ID.
        self.region_id = region_id
        # The grouping key. If this parameter is left empty, the default value is region, and the aggregated data is returned. You can specify multiple values separated by commas (,). Valid values:
        # - domain: the domain name. If SplitBy is set to domain, the Domain field in the response takes effect.
        # - region (default): the live center region. If SplitBy is set to region, the Region field in the response takes effect.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. By default, data from the last seven days is returned.
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

