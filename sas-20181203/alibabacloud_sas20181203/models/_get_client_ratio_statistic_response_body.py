# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetClientRatioStatisticResponseBody(DaraModel):
    def __init__(
        self,
        client_install_ratio: main_models.GetClientRatioStatisticResponseBodyClientInstallRatio = None,
        client_online_ratio: main_models.GetClientRatioStatisticResponseBodyClientOnlineRatio = None,
        dates: List[int] = None,
        request_id: str = None,
    ):
        # The statistics on the client installation rate.
        self.client_install_ratio = client_install_ratio
        # The statistics on the client online rate.
        self.client_online_ratio = client_online_ratio
        # The list of time when statistics were collected.
        self.dates = dates
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.client_install_ratio:
            self.client_install_ratio.validate()
        if self.client_online_ratio:
            self.client_online_ratio.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_install_ratio is not None:
            result['ClientInstallRatio'] = self.client_install_ratio.to_map()

        if self.client_online_ratio is not None:
            result['ClientOnlineRatio'] = self.client_online_ratio.to_map()

        if self.dates is not None:
            result['Dates'] = self.dates

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInstallRatio') is not None:
            temp_model = main_models.GetClientRatioStatisticResponseBodyClientInstallRatio()
            self.client_install_ratio = temp_model.from_map(m.get('ClientInstallRatio'))

        if m.get('ClientOnlineRatio') is not None:
            temp_model = main_models.GetClientRatioStatisticResponseBodyClientOnlineRatio()
            self.client_online_ratio = temp_model.from_map(m.get('ClientOnlineRatio'))

        if m.get('Dates') is not None:
            self.dates = m.get('Dates')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetClientRatioStatisticResponseBodyClientOnlineRatio(DaraModel):
    def __init__(
        self,
        current_items: List[main_models.GetClientRatioStatisticResponseBodyClientOnlineRatioCurrentItems] = None,
        history_items: List[main_models.GetClientRatioStatisticResponseBodyClientOnlineRatioHistoryItems] = None,
    ):
        # The list of current statistics on the online rate of the client.
        self.current_items = current_items
        # The list of historical statistics on the online rate of the client.
        self.history_items = history_items

    def validate(self):
        if self.current_items:
            for v1 in self.current_items:
                 if v1:
                    v1.validate()
        if self.history_items:
            for v1 in self.history_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CurrentItems'] = []
        if self.current_items is not None:
            for k1 in self.current_items:
                result['CurrentItems'].append(k1.to_map() if k1 else None)

        result['HistoryItems'] = []
        if self.history_items is not None:
            for k1 in self.history_items:
                result['HistoryItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.current_items = []
        if m.get('CurrentItems') is not None:
            for k1 in m.get('CurrentItems'):
                temp_model = main_models.GetClientRatioStatisticResponseBodyClientOnlineRatioCurrentItems()
                self.current_items.append(temp_model.from_map(k1))

        self.history_items = []
        if m.get('HistoryItems') is not None:
            for k1 in m.get('HistoryItems'):
                temp_model = main_models.GetClientRatioStatisticResponseBodyClientOnlineRatioHistoryItems()
                self.history_items.append(temp_model.from_map(k1))

        return self

class GetClientRatioStatisticResponseBodyClientOnlineRatioHistoryItems(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetClientRatioStatisticResponseBodyClientOnlineRatioHistoryItemsItems] = None,
        vendor: int = None,
    ):
        # The list of historical statistics on the online rate of the client by vendor.
        self.items = items
        # The type of the server. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud
        # *   **1**: a third-party cloud asset
        # *   **2**: an asset in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a lightweight asset
        self.vendor = vendor

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetClientRatioStatisticResponseBodyClientOnlineRatioHistoryItemsItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class GetClientRatioStatisticResponseBodyClientOnlineRatioHistoryItemsItems(DaraModel):
    def __init__(
        self,
        asset_install_count: int = None,
        calculate_time: int = None,
        online_asset_count: int = None,
        online_ratio: float = None,
    ):
        # The number of assets on which the client is installed.
        self.asset_install_count = asset_install_count
        # The timestamp of the calculation. Unit: milliseconds.
        self.calculate_time = calculate_time
        # The number of online assets.
        self.online_asset_count = online_asset_count
        # The online rate. Unit: %.
        self.online_ratio = online_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_install_count is not None:
            result['AssetInstallCount'] = self.asset_install_count

        if self.calculate_time is not None:
            result['CalculateTime'] = self.calculate_time

        if self.online_asset_count is not None:
            result['OnlineAssetCount'] = self.online_asset_count

        if self.online_ratio is not None:
            result['OnlineRatio'] = self.online_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetInstallCount') is not None:
            self.asset_install_count = m.get('AssetInstallCount')

        if m.get('CalculateTime') is not None:
            self.calculate_time = m.get('CalculateTime')

        if m.get('OnlineAssetCount') is not None:
            self.online_asset_count = m.get('OnlineAssetCount')

        if m.get('OnlineRatio') is not None:
            self.online_ratio = m.get('OnlineRatio')

        return self

class GetClientRatioStatisticResponseBodyClientOnlineRatioCurrentItems(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetClientRatioStatisticResponseBodyClientOnlineRatioCurrentItemsItems] = None,
        vendor: int = None,
    ):
        # The list of current statistics on the online rate of the client by vendor.
        self.items = items
        # The type of the cloud asset. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud
        # *   **1**: a third-party cloud asset
        # *   **2**: an asset in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a simple application server
        self.vendor = vendor

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetClientRatioStatisticResponseBodyClientOnlineRatioCurrentItemsItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class GetClientRatioStatisticResponseBodyClientOnlineRatioCurrentItemsItems(DaraModel):
    def __init__(
        self,
        asset_install_count: int = None,
        calculate_time: int = None,
        online_asset_count: int = None,
        online_ratio: float = None,
    ):
        # The number of assets on which the client is installed.
        self.asset_install_count = asset_install_count
        # The timestamp of the calculation. Unit: milliseconds.
        self.calculate_time = calculate_time
        # The number of online assets.
        self.online_asset_count = online_asset_count
        # The online rate. Unit: %.
        self.online_ratio = online_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_install_count is not None:
            result['AssetInstallCount'] = self.asset_install_count

        if self.calculate_time is not None:
            result['CalculateTime'] = self.calculate_time

        if self.online_asset_count is not None:
            result['OnlineAssetCount'] = self.online_asset_count

        if self.online_ratio is not None:
            result['OnlineRatio'] = self.online_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetInstallCount') is not None:
            self.asset_install_count = m.get('AssetInstallCount')

        if m.get('CalculateTime') is not None:
            self.calculate_time = m.get('CalculateTime')

        if m.get('OnlineAssetCount') is not None:
            self.online_asset_count = m.get('OnlineAssetCount')

        if m.get('OnlineRatio') is not None:
            self.online_ratio = m.get('OnlineRatio')

        return self

class GetClientRatioStatisticResponseBodyClientInstallRatio(DaraModel):
    def __init__(
        self,
        current_items: List[main_models.GetClientRatioStatisticResponseBodyClientInstallRatioCurrentItems] = None,
        history_items: List[main_models.GetClientRatioStatisticResponseBodyClientInstallRatioHistoryItems] = None,
    ):
        # The list of current statistics on the installation rate of the client.
        self.current_items = current_items
        # The list of historical statistics on the installation rate of the client.
        self.history_items = history_items

    def validate(self):
        if self.current_items:
            for v1 in self.current_items:
                 if v1:
                    v1.validate()
        if self.history_items:
            for v1 in self.history_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CurrentItems'] = []
        if self.current_items is not None:
            for k1 in self.current_items:
                result['CurrentItems'].append(k1.to_map() if k1 else None)

        result['HistoryItems'] = []
        if self.history_items is not None:
            for k1 in self.history_items:
                result['HistoryItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.current_items = []
        if m.get('CurrentItems') is not None:
            for k1 in m.get('CurrentItems'):
                temp_model = main_models.GetClientRatioStatisticResponseBodyClientInstallRatioCurrentItems()
                self.current_items.append(temp_model.from_map(k1))

        self.history_items = []
        if m.get('HistoryItems') is not None:
            for k1 in m.get('HistoryItems'):
                temp_model = main_models.GetClientRatioStatisticResponseBodyClientInstallRatioHistoryItems()
                self.history_items.append(temp_model.from_map(k1))

        return self

class GetClientRatioStatisticResponseBodyClientInstallRatioHistoryItems(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetClientRatioStatisticResponseBodyClientInstallRatioHistoryItemsItems] = None,
        vendor: int = None,
    ):
        # The list of statistics on the client installation rate.
        self.items = items
        # The type of the cloud asset. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud
        # *   **1**: a third-party cloud asset
        # *   **2**: an asset in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a simple application server
        self.vendor = vendor

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetClientRatioStatisticResponseBodyClientInstallRatioHistoryItemsItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class GetClientRatioStatisticResponseBodyClientInstallRatioHistoryItemsItems(DaraModel):
    def __init__(
        self,
        asset_total_count: int = None,
        calculate_time: int = None,
        install_ratio: float = None,
        installed_asset_count: int = None,
    ):
        # The total number of assets.
        self.asset_total_count = asset_total_count
        # The timestamp of the calculation. Unit: milliseconds.
        self.calculate_time = calculate_time
        # The installation rate. Unit: %.
        self.install_ratio = install_ratio
        # The number of assets on which the client is installed.
        self.installed_asset_count = installed_asset_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_total_count is not None:
            result['AssetTotalCount'] = self.asset_total_count

        if self.calculate_time is not None:
            result['CalculateTime'] = self.calculate_time

        if self.install_ratio is not None:
            result['InstallRatio'] = self.install_ratio

        if self.installed_asset_count is not None:
            result['InstalledAssetCount'] = self.installed_asset_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetTotalCount') is not None:
            self.asset_total_count = m.get('AssetTotalCount')

        if m.get('CalculateTime') is not None:
            self.calculate_time = m.get('CalculateTime')

        if m.get('InstallRatio') is not None:
            self.install_ratio = m.get('InstallRatio')

        if m.get('InstalledAssetCount') is not None:
            self.installed_asset_count = m.get('InstalledAssetCount')

        return self

class GetClientRatioStatisticResponseBodyClientInstallRatioCurrentItems(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetClientRatioStatisticResponseBodyClientInstallRatioCurrentItemsItems] = None,
        vendor: int = None,
    ):
        # The list of the statistics on the installation rate of the client by vendor.
        self.items = items
        # The type of the server. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud
        # *   **1**: a third-party cloud asset
        # *   **2**: an asset in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a lightweight asset
        self.vendor = vendor

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetClientRatioStatisticResponseBodyClientInstallRatioCurrentItemsItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class GetClientRatioStatisticResponseBodyClientInstallRatioCurrentItemsItems(DaraModel):
    def __init__(
        self,
        asset_total_count: int = None,
        calculate_time: int = None,
        install_ratio: float = None,
        installed_asset_count: int = None,
    ):
        # The total number of assets.
        self.asset_total_count = asset_total_count
        # The timestamp of the calculation. Unit: milliseconds.
        self.calculate_time = calculate_time
        # The installation rate. Unit: %.
        self.install_ratio = install_ratio
        # The number of assets on which the client is installed.
        self.installed_asset_count = installed_asset_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_total_count is not None:
            result['AssetTotalCount'] = self.asset_total_count

        if self.calculate_time is not None:
            result['CalculateTime'] = self.calculate_time

        if self.install_ratio is not None:
            result['InstallRatio'] = self.install_ratio

        if self.installed_asset_count is not None:
            result['InstalledAssetCount'] = self.installed_asset_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetTotalCount') is not None:
            self.asset_total_count = m.get('AssetTotalCount')

        if m.get('CalculateTime') is not None:
            self.calculate_time = m.get('CalculateTime')

        if m.get('InstallRatio') is not None:
            self.install_ratio = m.get('InstallRatio')

        if m.get('InstalledAssetCount') is not None:
            self.installed_asset_count = m.get('InstalledAssetCount')

        return self

