# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetOriginProtectionResponseBody(DaraModel):
    def __init__(
        self,
        auto_confirm_iplist: str = None,
        current_ipwhitelist: main_models.GetOriginProtectionResponseBodyCurrentIPWhitelist = None,
        diff_ipwhitelist: main_models.GetOriginProtectionResponseBodyDiffIPWhitelist = None,
        latest_ipwhitelist: main_models.GetOriginProtectionResponseBodyLatestIPWhitelist = None,
        need_update: bool = None,
        origin_converge: str = None,
        origin_protection: str = None,
        regional_current_ipwhitelist: main_models.GetOriginProtectionResponseBodyRegionalCurrentIPWhitelist = None,
        regional_diff_ipwhitelist: main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelist = None,
        regional_latest_ipwhitelist: main_models.GetOriginProtectionResponseBodyRegionalLatestIPWhitelist = None,
        request_id: str = None,
        site_id: int = None,
    ):
        self.auto_confirm_iplist = auto_confirm_iplist
        # The IP whitelist for origin protection used by the website.
        self.current_ipwhitelist = current_ipwhitelist
        # The IP whitelist for origin protection that has been updated.
        self.diff_ipwhitelist = diff_ipwhitelist
        # The latest IP whitelist for origin protection.
        self.latest_ipwhitelist = latest_ipwhitelist
        # Indicates whether the IP whitelist for origin protection needs to be updated. If the currently used IP whitelist is different from the latest IP whitelist, it needs to be updated, and the value is true.
        # 
        # *   true: The update is required.
        # *   false: No update is required.
        self.need_update = need_update
        # Indicates whether IP convergence is enabled.
        # 
        # *   on
        # *   off
        self.origin_converge = origin_converge
        # Indicates whether origin protection is enabled.
        # 
        # *   on
        # *   off
        self.origin_protection = origin_protection
        self.regional_current_ipwhitelist = regional_current_ipwhitelist
        self.regional_diff_ipwhitelist = regional_diff_ipwhitelist
        self.regional_latest_ipwhitelist = regional_latest_ipwhitelist
        # The request ID.
        self.request_id = request_id
        # The website ID.
        self.site_id = site_id

    def validate(self):
        if self.current_ipwhitelist:
            self.current_ipwhitelist.validate()
        if self.diff_ipwhitelist:
            self.diff_ipwhitelist.validate()
        if self.latest_ipwhitelist:
            self.latest_ipwhitelist.validate()
        if self.regional_current_ipwhitelist:
            self.regional_current_ipwhitelist.validate()
        if self.regional_diff_ipwhitelist:
            self.regional_diff_ipwhitelist.validate()
        if self.regional_latest_ipwhitelist:
            self.regional_latest_ipwhitelist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_confirm_iplist is not None:
            result['AutoConfirmIPList'] = self.auto_confirm_iplist

        if self.current_ipwhitelist is not None:
            result['CurrentIPWhitelist'] = self.current_ipwhitelist.to_map()

        if self.diff_ipwhitelist is not None:
            result['DiffIPWhitelist'] = self.diff_ipwhitelist.to_map()

        if self.latest_ipwhitelist is not None:
            result['LatestIPWhitelist'] = self.latest_ipwhitelist.to_map()

        if self.need_update is not None:
            result['NeedUpdate'] = self.need_update

        if self.origin_converge is not None:
            result['OriginConverge'] = self.origin_converge

        if self.origin_protection is not None:
            result['OriginProtection'] = self.origin_protection

        if self.regional_current_ipwhitelist is not None:
            result['RegionalCurrentIPWhitelist'] = self.regional_current_ipwhitelist.to_map()

        if self.regional_diff_ipwhitelist is not None:
            result['RegionalDiffIPWhitelist'] = self.regional_diff_ipwhitelist.to_map()

        if self.regional_latest_ipwhitelist is not None:
            result['RegionalLatestIPWhitelist'] = self.regional_latest_ipwhitelist.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoConfirmIPList') is not None:
            self.auto_confirm_iplist = m.get('AutoConfirmIPList')

        if m.get('CurrentIPWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyCurrentIPWhitelist()
            self.current_ipwhitelist = temp_model.from_map(m.get('CurrentIPWhitelist'))

        if m.get('DiffIPWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyDiffIPWhitelist()
            self.diff_ipwhitelist = temp_model.from_map(m.get('DiffIPWhitelist'))

        if m.get('LatestIPWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyLatestIPWhitelist()
            self.latest_ipwhitelist = temp_model.from_map(m.get('LatestIPWhitelist'))

        if m.get('NeedUpdate') is not None:
            self.need_update = m.get('NeedUpdate')

        if m.get('OriginConverge') is not None:
            self.origin_converge = m.get('OriginConverge')

        if m.get('OriginProtection') is not None:
            self.origin_protection = m.get('OriginProtection')

        if m.get('RegionalCurrentIPWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyRegionalCurrentIPWhitelist()
            self.regional_current_ipwhitelist = temp_model.from_map(m.get('RegionalCurrentIPWhitelist'))

        if m.get('RegionalDiffIPWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelist()
            self.regional_diff_ipwhitelist = temp_model.from_map(m.get('RegionalDiffIPWhitelist'))

        if m.get('RegionalLatestIPWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyRegionalLatestIPWhitelist()
            self.regional_latest_ipwhitelist = temp_model.from_map(m.get('RegionalLatestIPWhitelist'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

class GetOriginProtectionResponseBodyRegionalLatestIPWhitelist(DaraModel):
    def __init__(
        self,
        regional_ipv_4: List[main_models.GetOriginProtectionResponseBodyRegionalLatestIPWhitelistRegionalIPv4] = None,
        regional_ipv_6: List[main_models.GetOriginProtectionResponseBodyRegionalLatestIPWhitelistRegionalIPv6] = None,
    ):
        self.regional_ipv_4 = regional_ipv_4
        self.regional_ipv_6 = regional_ipv_6

    def validate(self):
        if self.regional_ipv_4:
            for v1 in self.regional_ipv_4:
                 if v1:
                    v1.validate()
        if self.regional_ipv_6:
            for v1 in self.regional_ipv_6:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionalIPv4'] = []
        if self.regional_ipv_4 is not None:
            for k1 in self.regional_ipv_4:
                result['RegionalIPv4'].append(k1.to_map() if k1 else None)

        result['RegionalIPv6'] = []
        if self.regional_ipv_6 is not None:
            for k1 in self.regional_ipv_6:
                result['RegionalIPv6'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regional_ipv_4 = []
        if m.get('RegionalIPv4') is not None:
            for k1 in m.get('RegionalIPv4'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalLatestIPWhitelistRegionalIPv4()
                self.regional_ipv_4.append(temp_model.from_map(k1))

        self.regional_ipv_6 = []
        if m.get('RegionalIPv6') is not None:
            for k1 in m.get('RegionalIPv6'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalLatestIPWhitelistRegionalIPv6()
                self.regional_ipv_6.append(temp_model.from_map(k1))

        return self

class GetOriginProtectionResponseBodyRegionalLatestIPWhitelistRegionalIPv6(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyRegionalLatestIPWhitelistRegionalIPv4(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelist(DaraModel):
    def __init__(
        self,
        added_ipregion_whitelist: main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistAddedIPRegionWhitelist = None,
        no_change_ip_whitelist: main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistNoChangeIpWhitelist = None,
        removed_ipregion_whitelist: main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistRemovedIPRegionWhitelist = None,
    ):
        self.added_ipregion_whitelist = added_ipregion_whitelist
        self.no_change_ip_whitelist = no_change_ip_whitelist
        self.removed_ipregion_whitelist = removed_ipregion_whitelist

    def validate(self):
        if self.added_ipregion_whitelist:
            self.added_ipregion_whitelist.validate()
        if self.no_change_ip_whitelist:
            self.no_change_ip_whitelist.validate()
        if self.removed_ipregion_whitelist:
            self.removed_ipregion_whitelist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.added_ipregion_whitelist is not None:
            result['AddedIPRegionWhitelist'] = self.added_ipregion_whitelist.to_map()

        if self.no_change_ip_whitelist is not None:
            result['NoChangeIpWhitelist'] = self.no_change_ip_whitelist.to_map()

        if self.removed_ipregion_whitelist is not None:
            result['RemovedIPRegionWhitelist'] = self.removed_ipregion_whitelist.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddedIPRegionWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistAddedIPRegionWhitelist()
            self.added_ipregion_whitelist = temp_model.from_map(m.get('AddedIPRegionWhitelist'))

        if m.get('NoChangeIpWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistNoChangeIpWhitelist()
            self.no_change_ip_whitelist = temp_model.from_map(m.get('NoChangeIpWhitelist'))

        if m.get('RemovedIPRegionWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistRemovedIPRegionWhitelist()
            self.removed_ipregion_whitelist = temp_model.from_map(m.get('RemovedIPRegionWhitelist'))

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelistRemovedIPRegionWhitelist(DaraModel):
    def __init__(
        self,
        regional_ipv_4: List[main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistRemovedIPRegionWhitelistRegionalIPv4] = None,
        regional_ipv_6: List[main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistRemovedIPRegionWhitelistRegionalIPv6] = None,
    ):
        self.regional_ipv_4 = regional_ipv_4
        self.regional_ipv_6 = regional_ipv_6

    def validate(self):
        if self.regional_ipv_4:
            for v1 in self.regional_ipv_4:
                 if v1:
                    v1.validate()
        if self.regional_ipv_6:
            for v1 in self.regional_ipv_6:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionalIPv4'] = []
        if self.regional_ipv_4 is not None:
            for k1 in self.regional_ipv_4:
                result['RegionalIPv4'].append(k1.to_map() if k1 else None)

        result['RegionalIPv6'] = []
        if self.regional_ipv_6 is not None:
            for k1 in self.regional_ipv_6:
                result['RegionalIPv6'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regional_ipv_4 = []
        if m.get('RegionalIPv4') is not None:
            for k1 in m.get('RegionalIPv4'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistRemovedIPRegionWhitelistRegionalIPv4()
                self.regional_ipv_4.append(temp_model.from_map(k1))

        self.regional_ipv_6 = []
        if m.get('RegionalIPv6') is not None:
            for k1 in m.get('RegionalIPv6'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistRemovedIPRegionWhitelistRegionalIPv6()
                self.regional_ipv_6.append(temp_model.from_map(k1))

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelistRemovedIPRegionWhitelistRegionalIPv6(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelistRemovedIPRegionWhitelistRegionalIPv4(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelistNoChangeIpWhitelist(DaraModel):
    def __init__(
        self,
        regional_ipv_4: List[main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistNoChangeIpWhitelistRegionalIPv4] = None,
        regional_ipv_6: List[main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistNoChangeIpWhitelistRegionalIPv6] = None,
    ):
        self.regional_ipv_4 = regional_ipv_4
        self.regional_ipv_6 = regional_ipv_6

    def validate(self):
        if self.regional_ipv_4:
            for v1 in self.regional_ipv_4:
                 if v1:
                    v1.validate()
        if self.regional_ipv_6:
            for v1 in self.regional_ipv_6:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionalIPv4'] = []
        if self.regional_ipv_4 is not None:
            for k1 in self.regional_ipv_4:
                result['RegionalIPv4'].append(k1.to_map() if k1 else None)

        result['RegionalIPv6'] = []
        if self.regional_ipv_6 is not None:
            for k1 in self.regional_ipv_6:
                result['RegionalIPv6'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regional_ipv_4 = []
        if m.get('RegionalIPv4') is not None:
            for k1 in m.get('RegionalIPv4'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistNoChangeIpWhitelistRegionalIPv4()
                self.regional_ipv_4.append(temp_model.from_map(k1))

        self.regional_ipv_6 = []
        if m.get('RegionalIPv6') is not None:
            for k1 in m.get('RegionalIPv6'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistNoChangeIpWhitelistRegionalIPv6()
                self.regional_ipv_6.append(temp_model.from_map(k1))

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelistNoChangeIpWhitelistRegionalIPv6(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelistNoChangeIpWhitelistRegionalIPv4(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelistAddedIPRegionWhitelist(DaraModel):
    def __init__(
        self,
        regional_ipv_4: List[main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistAddedIPRegionWhitelistRegionalIPv4] = None,
        regional_ipv_6: List[main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistAddedIPRegionWhitelistRegionalIPv6] = None,
    ):
        self.regional_ipv_4 = regional_ipv_4
        self.regional_ipv_6 = regional_ipv_6

    def validate(self):
        if self.regional_ipv_4:
            for v1 in self.regional_ipv_4:
                 if v1:
                    v1.validate()
        if self.regional_ipv_6:
            for v1 in self.regional_ipv_6:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionalIPv4'] = []
        if self.regional_ipv_4 is not None:
            for k1 in self.regional_ipv_4:
                result['RegionalIPv4'].append(k1.to_map() if k1 else None)

        result['RegionalIPv6'] = []
        if self.regional_ipv_6 is not None:
            for k1 in self.regional_ipv_6:
                result['RegionalIPv6'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regional_ipv_4 = []
        if m.get('RegionalIPv4') is not None:
            for k1 in m.get('RegionalIPv4'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistAddedIPRegionWhitelistRegionalIPv4()
                self.regional_ipv_4.append(temp_model.from_map(k1))

        self.regional_ipv_6 = []
        if m.get('RegionalIPv6') is not None:
            for k1 in m.get('RegionalIPv6'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalDiffIPWhitelistAddedIPRegionWhitelistRegionalIPv6()
                self.regional_ipv_6.append(temp_model.from_map(k1))

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelistAddedIPRegionWhitelistRegionalIPv6(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyRegionalDiffIPWhitelistAddedIPRegionWhitelistRegionalIPv4(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyRegionalCurrentIPWhitelist(DaraModel):
    def __init__(
        self,
        regional_ipv_4: List[main_models.GetOriginProtectionResponseBodyRegionalCurrentIPWhitelistRegionalIPv4] = None,
        regional_ipv_6: List[main_models.GetOriginProtectionResponseBodyRegionalCurrentIPWhitelistRegionalIPv6] = None,
    ):
        self.regional_ipv_4 = regional_ipv_4
        self.regional_ipv_6 = regional_ipv_6

    def validate(self):
        if self.regional_ipv_4:
            for v1 in self.regional_ipv_4:
                 if v1:
                    v1.validate()
        if self.regional_ipv_6:
            for v1 in self.regional_ipv_6:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionalIPv4'] = []
        if self.regional_ipv_4 is not None:
            for k1 in self.regional_ipv_4:
                result['RegionalIPv4'].append(k1.to_map() if k1 else None)

        result['RegionalIPv6'] = []
        if self.regional_ipv_6 is not None:
            for k1 in self.regional_ipv_6:
                result['RegionalIPv6'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regional_ipv_4 = []
        if m.get('RegionalIPv4') is not None:
            for k1 in m.get('RegionalIPv4'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalCurrentIPWhitelistRegionalIPv4()
                self.regional_ipv_4.append(temp_model.from_map(k1))

        self.regional_ipv_6 = []
        if m.get('RegionalIPv6') is not None:
            for k1 in m.get('RegionalIPv6'):
                temp_model = main_models.GetOriginProtectionResponseBodyRegionalCurrentIPWhitelistRegionalIPv6()
                self.regional_ipv_6.append(temp_model.from_map(k1))

        return self

class GetOriginProtectionResponseBodyRegionalCurrentIPWhitelistRegionalIPv6(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyRegionalCurrentIPWhitelistRegionalIPv4(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        region: str = None,
    ):
        self.cidr = cidr
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class GetOriginProtectionResponseBodyLatestIPWhitelist(DaraModel):
    def __init__(
        self,
        ipv_4: List[str] = None,
        ipv_6: List[str] = None,
    ):
        # The latest IP whitelist for origin protection, specified as IPv4 addresses or CIDR blocks.
        self.ipv_4 = ipv_4
        # The latest IP whitelist for origin protection, specified as IPv6 addresses or CIDR blocks.
        self.ipv_6 = ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4 is not None:
            result['IPv4'] = self.ipv_4

        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPv4') is not None:
            self.ipv_4 = m.get('IPv4')

        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')

        return self

class GetOriginProtectionResponseBodyDiffIPWhitelist(DaraModel):
    def __init__(
        self,
        added_ipwhitelist: main_models.GetOriginProtectionResponseBodyDiffIPWhitelistAddedIPWhitelist = None,
        no_change_ip_whitelist: main_models.GetOriginProtectionResponseBodyDiffIPWhitelistNoChangeIpWhitelist = None,
        removed_ipwhitelist: main_models.GetOriginProtectionResponseBodyDiffIPWhitelistRemovedIPWhitelist = None,
    ):
        # The new IP whitelist for origin protection.
        self.added_ipwhitelist = added_ipwhitelist
        # The IP whitelist for origin protection that remains unchanged.
        self.no_change_ip_whitelist = no_change_ip_whitelist
        # The IP whitelist for origin protection that has been deleted.
        self.removed_ipwhitelist = removed_ipwhitelist

    def validate(self):
        if self.added_ipwhitelist:
            self.added_ipwhitelist.validate()
        if self.no_change_ip_whitelist:
            self.no_change_ip_whitelist.validate()
        if self.removed_ipwhitelist:
            self.removed_ipwhitelist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.added_ipwhitelist is not None:
            result['AddedIPWhitelist'] = self.added_ipwhitelist.to_map()

        if self.no_change_ip_whitelist is not None:
            result['NoChangeIpWhitelist'] = self.no_change_ip_whitelist.to_map()

        if self.removed_ipwhitelist is not None:
            result['RemovedIPWhitelist'] = self.removed_ipwhitelist.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddedIPWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyDiffIPWhitelistAddedIPWhitelist()
            self.added_ipwhitelist = temp_model.from_map(m.get('AddedIPWhitelist'))

        if m.get('NoChangeIpWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyDiffIPWhitelistNoChangeIpWhitelist()
            self.no_change_ip_whitelist = temp_model.from_map(m.get('NoChangeIpWhitelist'))

        if m.get('RemovedIPWhitelist') is not None:
            temp_model = main_models.GetOriginProtectionResponseBodyDiffIPWhitelistRemovedIPWhitelist()
            self.removed_ipwhitelist = temp_model.from_map(m.get('RemovedIPWhitelist'))

        return self

class GetOriginProtectionResponseBodyDiffIPWhitelistRemovedIPWhitelist(DaraModel):
    def __init__(
        self,
        ipv_4: List[str] = None,
        ipv_6: List[str] = None,
    ):
        # The IP whitelist for origin protection, specified as IPv4 addresses or CIDR blocks.
        self.ipv_4 = ipv_4
        # The IP whitelist for origin protection, specified as IPv6 addresses or CIDR blocks.
        self.ipv_6 = ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4 is not None:
            result['IPv4'] = self.ipv_4

        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPv4') is not None:
            self.ipv_4 = m.get('IPv4')

        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')

        return self

class GetOriginProtectionResponseBodyDiffIPWhitelistNoChangeIpWhitelist(DaraModel):
    def __init__(
        self,
        ipv_4: List[str] = None,
        ipv_6: List[str] = None,
    ):
        # The IP whitelist for origin protection, specified as IPv4 addresses or CIDR blocks.
        self.ipv_4 = ipv_4
        # The IP whitelist for origin protection, specified as IPv6 addresses or CIDR blocks.
        self.ipv_6 = ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4 is not None:
            result['IPv4'] = self.ipv_4

        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPv4') is not None:
            self.ipv_4 = m.get('IPv4')

        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')

        return self

class GetOriginProtectionResponseBodyDiffIPWhitelistAddedIPWhitelist(DaraModel):
    def __init__(
        self,
        ipv_4: List[str] = None,
        ipv_6: List[str] = None,
    ):
        # The IP whitelist for origin protection, specified as IPv4 addresses or CIDR blocks.
        self.ipv_4 = ipv_4
        # The IP whitelist for origin protection, specified as IPv6 addresses or CIDR blocks.
        self.ipv_6 = ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4 is not None:
            result['IPv4'] = self.ipv_4

        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPv4') is not None:
            self.ipv_4 = m.get('IPv4')

        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')

        return self

class GetOriginProtectionResponseBodyCurrentIPWhitelist(DaraModel):
    def __init__(
        self,
        ipv_4: List[str] = None,
        ipv_6: List[str] = None,
    ):
        # The IP whitelist for origin protection used by the website, specified as IPv4 addresses or CIDR blocks.
        self.ipv_4 = ipv_4
        # The IP whitelist for origin protection used by the website, specified as IPv6 addresses or CIDR blocks.
        self.ipv_6 = ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4 is not None:
            result['IPv4'] = self.ipv_4

        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPv4') is not None:
            self.ipv_4 = m.get('IPv4')

        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')

        return self

