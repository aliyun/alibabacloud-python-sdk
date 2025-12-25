# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeCollationTimeZonesResponseBody(DaraModel):
    def __init__(
        self,
        collation_time_zones: main_models.DescribeCollationTimeZonesResponseBodyCollationTimeZones = None,
        request_id: str = None,
    ):
        # The list of the character set collations and time zones that are available.
        self.collation_time_zones = collation_time_zones
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.collation_time_zones:
            self.collation_time_zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collation_time_zones is not None:
            result['CollationTimeZones'] = self.collation_time_zones.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollationTimeZones') is not None:
            temp_model = main_models.DescribeCollationTimeZonesResponseBodyCollationTimeZones()
            self.collation_time_zones = temp_model.from_map(m.get('CollationTimeZones'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCollationTimeZonesResponseBodyCollationTimeZones(DaraModel):
    def __init__(
        self,
        collation_time_zone: List[main_models.DescribeCollationTimeZonesResponseBodyCollationTimeZonesCollationTimeZone] = None,
    ):
        self.collation_time_zone = collation_time_zone

    def validate(self):
        if self.collation_time_zone:
            for v1 in self.collation_time_zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CollationTimeZone'] = []
        if self.collation_time_zone is not None:
            for k1 in self.collation_time_zone:
                result['CollationTimeZone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.collation_time_zone = []
        if m.get('CollationTimeZone') is not None:
            for k1 in m.get('CollationTimeZone'):
                temp_model = main_models.DescribeCollationTimeZonesResponseBodyCollationTimeZonesCollationTimeZone()
                self.collation_time_zone.append(temp_model.from_map(k1))

        return self

class DescribeCollationTimeZonesResponseBodyCollationTimeZonesCollationTimeZone(DaraModel):
    def __init__(
        self,
        description: str = None,
        standard_time_offset: str = None,
        time_zone: str = None,
    ):
        # The description.
        self.description = description
        # The offset of the UTC time. The offset is in the following format: (UTC+*HH:mm*).
        self.standard_time_offset = standard_time_offset
        # The time zone.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.standard_time_offset is not None:
            result['StandardTimeOffset'] = self.standard_time_offset

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('StandardTimeOffset') is not None:
            self.standard_time_offset = m.get('StandardTimeOffset')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

