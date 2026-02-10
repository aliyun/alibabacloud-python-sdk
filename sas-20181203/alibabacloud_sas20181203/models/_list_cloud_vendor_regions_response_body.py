# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCloudVendorRegionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.ListCloudVendorRegionsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return code.
        self.code = code
        # The total number of returned entries.
        self.count = count
        # The regions that the service provider supports.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCloudVendorRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCloudVendorRegionsResponseBodyData(DaraModel):
    def __init__(
        self,
        area: str = None,
        disable: int = None,
        region_id: str = None,
        selected: int = None,
    ):
        # The area to which the region belongs. The valid values vary based on the value of the Vendor parameter.
        # 
        # *   Valid values if **Vendor** is set to Tencent:
        # *   **cn**: China
        # *   **southeast_asia**: Southeast Asia Pacific
        # *   **northeast_asia**: Northeast Asia Pacific
        # *   **southern_asia**: South Asia Pacific
        # *   **north_America**: North America
        # *   **south_America**: South America
        # *   **western_America**: Western United States
        # *   **eastern_America**: Eastern United States
        # *   **european**: Europe
        # *   Valid values if **Vendor** is set to HUAWEICLOUD:
        # *   **cn**: China
        # *   **africa**: Africa
        # *   **latin_america**: Latin America
        # *   **asia**: Asia Pacific
        # *   Valid values if **Vendor** is set to Azure:
        # *   **middle_east**: Middle East
        # *   **south_america**: South America
        # *   **canada**: Canada
        # *   **asia-pacific**: Asia Pacific
        # *   **europe**: Europe
        # *   **africa**: Africa
        # *   **us**: United States
        # *   **other**: other regions
        # *   Valid values if **Vendor** is set to AWS:
        # *   **cn**: China
        # *   **us**: United States
        # *   **eu**: Europe
        # *   **asia**: Asia Pacific
        # *   **south_america**: South America
        # *   **me**: Middle East
        # *   **ca**: Canada
        # *   **af**: Africa
        self.area = area
        # Indicates whether the region is configured as a synchronization region on another site. Valid values:
        # 
        # *   **0**: The region is not configured as a synchronization region on another site.
        # *   **1**: The region is configured as a synchronization region on another site.
        self.disable = disable
        # The region ID.
        self.region_id = region_id
        # Indicates whether the region is configured as a synchronization region on this site. Valid values:
        # 
        # *   **0**: The region is not configured as a synchronization region on this site.
        # *   **1**: The region is configured as a synchronization region on this site.
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.disable is not None:
            result['Disable'] = self.disable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.selected is not None:
            result['Selected'] = self.selected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('Disable') is not None:
            self.disable = m.get('Disable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        return self

