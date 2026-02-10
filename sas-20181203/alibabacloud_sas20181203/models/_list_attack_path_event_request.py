# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAttackPathEventRequest(DaraModel):
    def __init__(
        self,
        attack_path_asset_list: List[main_models.ListAttackPathEventRequestAttackPathAssetList] = None,
        current_page: int = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        path_name_desc: str = None,
        path_type: str = None,
        risk_level_list: List[str] = None,
        start_time: int = None,
    ):
        # List of cloud product assets in the attack path.
        self.attack_path_asset_list = attack_path_asset_list
        # Specifies from which page of the returned results the query results should be displayed. The default value is 1, indicating that the display starts from the first page.
        self.current_page = current_page
        # Timestamp of the end time. Unit: milliseconds.
        self.end_time = end_time
        # Sets the language type for requests and received messages, with the default being **zh**. Values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The maximum number of data entries displayed per page in a paginated query. The default value is **20**.
        self.page_size = page_size
        # Description of the path name.
        # > You can call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query the path name description.
        self.path_name_desc = path_name_desc
        # Path type.
        # > You can call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query the path type.
        self.path_type = path_type
        # List of risk level information.
        self.risk_level_list = risk_level_list
        # Timestamp of the start time. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        if self.attack_path_asset_list:
            for v1 in self.attack_path_asset_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttackPathAssetList'] = []
        if self.attack_path_asset_list is not None:
            for k1 in self.attack_path_asset_list:
                result['AttackPathAssetList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path_name_desc is not None:
            result['PathNameDesc'] = self.path_name_desc

        if self.path_type is not None:
            result['PathType'] = self.path_type

        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attack_path_asset_list = []
        if m.get('AttackPathAssetList') is not None:
            for k1 in m.get('AttackPathAssetList'):
                temp_model = main_models.ListAttackPathEventRequestAttackPathAssetList()
                self.attack_path_asset_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PathNameDesc') is not None:
            self.path_name_desc = m.get('PathNameDesc')

        if m.get('PathType') is not None:
            self.path_type = m.get('PathType')

        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListAttackPathEventRequestAttackPathAssetList(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        node_type: str = None,
        vendor: int = None,
    ):
        # Subtype of the cloud product asset.
        # 
        # > You can call [ListSupportAttackPathAsset](~~ListSupportAttackPathAsset~~) to query the subtype of the cloud product asset.
        self.asset_sub_type = asset_sub_type
        # Type of the cloud product asset.
        # 
        # > You can call [ListSupportAttackPathAsset](~~ListSupportAttackPathAsset~~) to query the type of the cloud product asset.
        self.asset_type = asset_type
        # Node type, values:
        # - **start**: start point.
        # - **end**: end point.
        self.node_type = node_type
        # Vendor of the cloud product asset.
        # > You can call [ListSupportAttackPathAsset](~~ListSupportAttackPathAsset~~) to query the vendor of the cloud product asset.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_sub_type is not None:
            result['AssetSubType'] = self.asset_sub_type

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

