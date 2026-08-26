# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDetectPornDataRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        domain_name: str = None,
        end_time: str = None,
        fee: str = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        scene: str = None,
        split_by: str = None,
        start_time: str = None,
        stream: str = None,
    ):
        # The name of the application to which the stream belongs.
        self.app = app
        # The streaming domain to query.
        # 
        # - You can query one or more domain names. To query multiple domain names, separate them with commas (,).
        # 
        # - If you do not specify this parameter, the service returns the merged data for all streaming domains.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.end_time = end_time
        # You have a daily free quota for image scans. Valid values:
        # 
        # - **free**
        # 
        # - **charge**
        self.fee = fee
        self.owner_id = owner_id
        # The region where the domain name is located.
        self.region = region
        # The region ID.
        self.region_id = region_id
        # The detection scenario. Valid values:
        # 
        # - **porn** (default): pornography detection.
        # 
        # - **terrorism**: terrorism and political content detection.
        # 
        # - **ad**: ad and text violation detection.
        # 
        # - **live**: undesirable live streaming scenario detection.
        # 
        # - **logo**: logo detection.
        self.scene = scene
        # The list of grouping fields. Separate multiple fields with commas (,).
        # 
        # > If you leave this parameter empty, the service returns only TimeStamp and Count.
        self.split_by = split_by
        # The start of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > - You can query data from the last 90 days.
        # 
        # - The minimum data granularity is 5 minutes. If you leave this parameter empty, the service queries data from the last 24 hours by default.
        self.start_time = start_time
        # The stream name.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fee is not None:
            result['Fee'] = self.fee

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.split_by is not None:
            result['SplitBy'] = self.split_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Fee') is not None:
            self.fee = m.get('Fee')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

