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
        # The name of the application to which the live stream belongs.
        self.app = app
        # The main streaming domain to query.
        # 
        # *   You can query one or more domain names. If you specify multiple domain names, separate them with commas (,).
        # *   If you do not specify this parameter, the data of all domain names within your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.end_time = end_time
        # Specifies whether a quota of free image scanning is available. Valid values:
        # 
        # *   **free**: specifies that a quota of free image scanning is available.
        # *   **charge**: specifies that a quota of free image scanning is not available and fees are charged.
        self.fee = fee
        self.owner_id = owner_id
        # The ID of the region where the domain name resides.
        self.region = region
        self.region_id = region_id
        # The moderation scenario. Valid values:
        # 
        # *   **porn**: pornography detection. This is the default value.
        # *   **terrorism**: terrorism detection
        # *   **ad**: ad violation detection
        # *   **live**: undesirable scene detection
        # *   **logo**: logo detection
        self.scene = scene
        # The fields based on which data is grouped. Separate multiple fields with commas (,).
        # 
        # > If you leave the **SplitBy** parameter empty, only the **TimeStamp** and **Count** parameters are returned.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > 
        # 
        # *   You can query data in the last 90 days.
        # 
        # *   The minimum data granularity is 5 minutes. If you do not specify this parameter, data in the last 24 hours is queried.
        self.start_time = start_time
        # The name of the live stream.
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

