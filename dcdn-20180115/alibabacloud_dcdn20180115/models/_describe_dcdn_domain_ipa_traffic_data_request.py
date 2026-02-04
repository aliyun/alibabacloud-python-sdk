# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDomainIpaTrafficDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        fix_time_gap: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        start_time: str = None,
        time_merge: str = None,
    ):
        # The accelerated domain name.
        # 
        # Separate multiple domain names with commas (,). If you do not specify a value for this parameter, data for all accelerated domain names is queried.
        self.domain_name = domain_name
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # Specify whether to implement padding with zeros. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fix_time_gap = fix_time_gap
        # The time granularity of data entries. Unit: seconds.
        # 
        # The time granularity varies with the time range specified by **StartTime** and **EndTime**.
        # 
        # *   If the time range between StartTime and EndTime is less than 3 days, the valid values are **300**, **3600**, and **86400**. If you do not specify a value for this parameter, **300** is used.
        # *   If the time range between StartTime and EndTime is greater than or equal to 3 days and less than 31 days, the valid values are **3600** and **86400**. Default value: **3600**.
        # *   If the time range between StartTime and EndTime is 31 days or longer, the valid value is **86400**. Default value: **86400**.
        self.interval = interval
        # The name of the Internet service provider (ISP).
        # 
        # You can call the [DescribeDcdnRegionAndIsp](https://help.aliyun.com/document_detail/207199.html) operation to query ISPs.
        self.isp_name_en = isp_name_en
        # The name of the region.
        # 
        # You can call the [DescribeDcdnRegionAndIsp](https://help.aliyun.com/document_detail/207199.html) operation to query regions.
        self.location_name_en = location_name_en
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # Specifies whether to automatically calculate the value of the **interval**. If the **timeMerge** parameter is set to **1**, the value of **inteval** is calculated based on **StartTime** and **EndTime**. You can set either this parameter or the **interval** parameter.
        self.time_merge = time_merge

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

        if self.fix_time_gap is not None:
            result['FixTimeGap'] = self.fix_time_gap

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en

        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_merge is not None:
            result['TimeMerge'] = self.time_merge

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FixTimeGap') is not None:
            self.fix_time_gap = m.get('FixTimeGap')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')

        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeMerge') is not None:
            self.time_merge = m.get('TimeMerge')

        return self

