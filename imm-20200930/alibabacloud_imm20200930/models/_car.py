# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Car(DaraModel):
    def __init__(
        self,
        boundary: main_models.Boundary = None,
        car_color: str = None,
        car_color_confidence: float = None,
        car_type: str = None,
        car_type_confidence: float = None,
        confidence: float = None,
        license_plates: List[main_models.LicensePlate] = None,
    ):
        # The boundary information.
        self.boundary = boundary
        # The vehicle color. Valid values
        # 
        # *   white
        # *   grey
        # *   yellow
        # *   red
        # *   green
        # *   blue
        # *   black
        # *   purple
        # *   brown
        self.car_color = car_color
        # The confidence level of the vehicle color. Valid values: 0 to 1. The value 0 indicates the lowest confidence level. The value 1 indicates the highest confidence level.
        self.car_color_confidence = car_color_confidence
        # The vehicle type. Valid values:
        # 
        # *   car
        # *   bus
        # *   truck
        # *   van
        self.car_type = car_type
        # The confidence level of the vehicle type. Valid values: 0 to 1. The value 0 indicates the lowest confidence level. The value 1 indicates the highest confidence level.
        self.car_type_confidence = car_type_confidence
        # The confidence level of the vehicle detection result. Valid values: 0 to 1. The value 0 indicates the lowest confidence level. The value 1 indicates the highest confidence level.
        self.confidence = confidence
        # The license plates.
        self.license_plates = license_plates

    def validate(self):
        if self.boundary:
            self.boundary.validate()
        if self.license_plates:
            for v1 in self.license_plates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()

        if self.car_color is not None:
            result['CarColor'] = self.car_color

        if self.car_color_confidence is not None:
            result['CarColorConfidence'] = self.car_color_confidence

        if self.car_type is not None:
            result['CarType'] = self.car_type

        if self.car_type_confidence is not None:
            result['CarTypeConfidence'] = self.car_type_confidence

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        result['LicensePlates'] = []
        if self.license_plates is not None:
            for k1 in self.license_plates:
                result['LicensePlates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = main_models.Boundary()
            self.boundary = temp_model.from_map(m.get('Boundary'))

        if m.get('CarColor') is not None:
            self.car_color = m.get('CarColor')

        if m.get('CarColorConfidence') is not None:
            self.car_color_confidence = m.get('CarColorConfidence')

        if m.get('CarType') is not None:
            self.car_type = m.get('CarType')

        if m.get('CarTypeConfidence') is not None:
            self.car_type_confidence = m.get('CarTypeConfidence')

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        self.license_plates = []
        if m.get('LicensePlates') is not None:
            for k1 in m.get('LicensePlates'):
                temp_model = main_models.LicensePlate()
                self.license_plates.append(temp_model.from_map(k1))

        return self

