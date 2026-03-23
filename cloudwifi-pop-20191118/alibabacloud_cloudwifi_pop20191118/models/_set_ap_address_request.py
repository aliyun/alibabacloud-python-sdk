# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetApAddressRequest(DaraModel):
    def __init__(
        self,
        ap_area_name: str = None,
        ap_building_name: str = None,
        ap_campus_name: str = None,
        ap_city_name: str = None,
        ap_floor: str = None,
        ap_group: str = None,
        ap_name: str = None,
        ap_nation_name: str = None,
        ap_province_name: str = None,
        ap_unit_id: int = None,
        ap_unit_name: str = None,
        app_code: str = None,
        app_name: str = None,
        direction: str = None,
        language: str = None,
        lat: str = None,
        lng: str = None,
        mac: str = None,
    ):
        self.ap_area_name = ap_area_name
        self.ap_building_name = ap_building_name
        self.ap_campus_name = ap_campus_name
        self.ap_city_name = ap_city_name
        self.ap_floor = ap_floor
        self.ap_group = ap_group
        self.ap_name = ap_name
        self.ap_nation_name = ap_nation_name
        self.ap_province_name = ap_province_name
        self.ap_unit_id = ap_unit_id
        self.ap_unit_name = ap_unit_name
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        self.direction = direction
        # This parameter is required.
        self.language = language
        self.lat = lat
        self.lng = lng
        # This parameter is required.
        self.mac = mac

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ap_area_name is not None:
            result['ApAreaName'] = self.ap_area_name

        if self.ap_building_name is not None:
            result['ApBuildingName'] = self.ap_building_name

        if self.ap_campus_name is not None:
            result['ApCampusName'] = self.ap_campus_name

        if self.ap_city_name is not None:
            result['ApCityName'] = self.ap_city_name

        if self.ap_floor is not None:
            result['ApFloor'] = self.ap_floor

        if self.ap_group is not None:
            result['ApGroup'] = self.ap_group

        if self.ap_name is not None:
            result['ApName'] = self.ap_name

        if self.ap_nation_name is not None:
            result['ApNationName'] = self.ap_nation_name

        if self.ap_province_name is not None:
            result['ApProvinceName'] = self.ap_province_name

        if self.ap_unit_id is not None:
            result['ApUnitId'] = self.ap_unit_id

        if self.ap_unit_name is not None:
            result['ApUnitName'] = self.ap_unit_name

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.language is not None:
            result['Language'] = self.language

        if self.lat is not None:
            result['Lat'] = self.lat

        if self.lng is not None:
            result['Lng'] = self.lng

        if self.mac is not None:
            result['Mac'] = self.mac

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApAreaName') is not None:
            self.ap_area_name = m.get('ApAreaName')

        if m.get('ApBuildingName') is not None:
            self.ap_building_name = m.get('ApBuildingName')

        if m.get('ApCampusName') is not None:
            self.ap_campus_name = m.get('ApCampusName')

        if m.get('ApCityName') is not None:
            self.ap_city_name = m.get('ApCityName')

        if m.get('ApFloor') is not None:
            self.ap_floor = m.get('ApFloor')

        if m.get('ApGroup') is not None:
            self.ap_group = m.get('ApGroup')

        if m.get('ApName') is not None:
            self.ap_name = m.get('ApName')

        if m.get('ApNationName') is not None:
            self.ap_nation_name = m.get('ApNationName')

        if m.get('ApProvinceName') is not None:
            self.ap_province_name = m.get('ApProvinceName')

        if m.get('ApUnitId') is not None:
            self.ap_unit_id = m.get('ApUnitId')

        if m.get('ApUnitName') is not None:
            self.ap_unit_name = m.get('ApUnitName')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Lat') is not None:
            self.lat = m.get('Lat')

        if m.get('Lng') is not None:
            self.lng = m.get('Lng')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        return self

