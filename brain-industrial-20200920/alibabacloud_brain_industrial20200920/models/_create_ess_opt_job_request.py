# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_brain_industrial20200920 import models as main_models
from darabonba.model import DaraModel

class CreateEssOptJobRequest(DaraModel):
    def __init__(
        self,
        business_key: str = None,
        duration: int = None,
        elec_price: List[main_models.CreateEssOptJobRequestElecPrice] = None,
        freq: str = None,
        gen_price: List[main_models.CreateEssOptJobRequestGenPrice] = None,
        location: main_models.CreateEssOptJobRequestLocation = None,
        model_version: str = None,
        run_date: str = None,
        system_data: List[main_models.CreateEssOptJobRequestSystemData] = None,
        time_zone: str = None,
        topo_type: str = None,
    ):
        self.business_key = business_key
        self.duration = duration
        self.elec_price = elec_price
        self.freq = freq
        self.gen_price = gen_price
        self.location = location
        self.model_version = model_version
        self.run_date = run_date
        self.system_data = system_data
        self.time_zone = time_zone
        self.topo_type = topo_type

    def validate(self):
        if self.elec_price:
            for v1 in self.elec_price:
                 if v1:
                    v1.validate()
        if self.gen_price:
            for v1 in self.gen_price:
                 if v1:
                    v1.validate()
        if self.location:
            self.location.validate()
        if self.system_data:
            for v1 in self.system_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_key is not None:
            result['BusinessKey'] = self.business_key

        if self.duration is not None:
            result['Duration'] = self.duration

        result['ElecPrice'] = []
        if self.elec_price is not None:
            for k1 in self.elec_price:
                result['ElecPrice'].append(k1.to_map() if k1 else None)

        if self.freq is not None:
            result['Freq'] = self.freq

        result['GenPrice'] = []
        if self.gen_price is not None:
            for k1 in self.gen_price:
                result['GenPrice'].append(k1.to_map() if k1 else None)

        if self.location is not None:
            result['Location'] = self.location.to_map()

        if self.model_version is not None:
            result['ModelVersion'] = self.model_version

        if self.run_date is not None:
            result['RunDate'] = self.run_date

        result['SystemData'] = []
        if self.system_data is not None:
            for k1 in self.system_data:
                result['SystemData'].append(k1.to_map() if k1 else None)

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.topo_type is not None:
            result['TopoType'] = self.topo_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessKey') is not None:
            self.business_key = m.get('BusinessKey')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        self.elec_price = []
        if m.get('ElecPrice') is not None:
            for k1 in m.get('ElecPrice'):
                temp_model = main_models.CreateEssOptJobRequestElecPrice()
                self.elec_price.append(temp_model.from_map(k1))

        if m.get('Freq') is not None:
            self.freq = m.get('Freq')

        self.gen_price = []
        if m.get('GenPrice') is not None:
            for k1 in m.get('GenPrice'):
                temp_model = main_models.CreateEssOptJobRequestGenPrice()
                self.gen_price.append(temp_model.from_map(k1))

        if m.get('Location') is not None:
            temp_model = main_models.CreateEssOptJobRequestLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')

        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')

        self.system_data = []
        if m.get('SystemData') is not None:
            for k1 in m.get('SystemData'):
                temp_model = main_models.CreateEssOptJobRequestSystemData()
                self.system_data.append(temp_model.from_map(k1))

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('TopoType') is not None:
            self.topo_type = m.get('TopoType')

        return self

class CreateEssOptJobRequestSystemData(DaraModel):
    def __init__(
        self,
        history_data: List[Dict[str, Any]] = None,
        system_id: str = None,
        system_params: Dict[str, Any] = None,
        system_type: str = None,
    ):
        self.history_data = history_data
        self.system_id = system_id
        self.system_params = system_params
        self.system_type = system_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.history_data is not None:
            result['HistoryData'] = self.history_data

        if self.system_id is not None:
            result['SystemId'] = self.system_id

        if self.system_params is not None:
            result['SystemParams'] = self.system_params

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryData') is not None:
            self.history_data = m.get('HistoryData')

        if m.get('SystemId') is not None:
            self.system_id = m.get('SystemId')

        if m.get('SystemParams') is not None:
            self.system_params = m.get('SystemParams')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        return self

class CreateEssOptJobRequestLocation(DaraModel):
    def __init__(
        self,
        altitude: float = None,
        latitude: float = None,
        longitude: float = None,
    ):
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.altitude is not None:
            result['Altitude'] = self.altitude

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Altitude') is not None:
            self.altitude = m.get('Altitude')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        return self

class CreateEssOptJobRequestGenPrice(DaraModel):
    def __init__(
        self,
        data_time: str = None,
        price: str = None,
    ):
        self.data_time = data_time
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.price is not None:
            result['Price'] = self.price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        return self

class CreateEssOptJobRequestElecPrice(DaraModel):
    def __init__(
        self,
        data_time: str = None,
        price: str = None,
    ):
        self.data_time = data_time
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.price is not None:
            result['Price'] = self.price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        return self

