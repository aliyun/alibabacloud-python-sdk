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
        # The list of cloud service assets in the attack path.
        self.attack_path_asset_list = attack_path_asset_list
        # The page number of the results to return. Default value: 1, which indicates the first page.
        self.current_page = current_page
        # The end time as a timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries per page in a paged query. Default value: **20**.
        self.page_size = page_size
        # The path name description.
        # > Call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query path name descriptions.
        self.path_name_desc = path_name_desc
        # The path type.
        # > Call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query path types.
        self.path_type = path_type
        # The list of risk levels.
        self.risk_level_list = risk_level_list
        # The start time as a timestamp. Unit: milliseconds.
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
        # The subtype of the cloud service asset.
        # 
        # > Call [ListSupportAttackPathAsset](~~ListSupportAttackPathAsset~~) to query the subtypes of cloud service assets.
        self.asset_sub_type = asset_sub_type
        # The type of the cloud service asset.
        # 
        # > Call [ListSupportAttackPathAsset](~~ListSupportAttackPathAsset~~) to query the types of cloud service assets.
        self.asset_type = asset_type
        # The node type. Valid values:
        # - **start**: start node.
        # - **end**: end node.
        self.node_type = node_type
        # The vendor of the cloud service asset.
        # > Call [ListSupportAttackPathAsset](~~ListSupportAttackPathAsset~~) to query the vendors of cloud service assets.
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

