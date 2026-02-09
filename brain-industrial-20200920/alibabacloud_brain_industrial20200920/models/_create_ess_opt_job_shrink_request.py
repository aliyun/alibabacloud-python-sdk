# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEssOptJobShrinkRequest(DaraModel):
    def __init__(
        self,
        business_key: str = None,
        duration: int = None,
        elec_price_shrink: str = None,
        freq: str = None,
        gen_price_shrink: str = None,
        location_shrink: str = None,
        model_version: str = None,
        run_date: str = None,
        system_data_shrink: str = None,
        time_zone: str = None,
        topo_type: str = None,
    ):
        self.business_key = business_key
        self.duration = duration
        self.elec_price_shrink = elec_price_shrink
        self.freq = freq
        self.gen_price_shrink = gen_price_shrink
        self.location_shrink = location_shrink
        self.model_version = model_version
        self.run_date = run_date
        self.system_data_shrink = system_data_shrink
        self.time_zone = time_zone
        self.topo_type = topo_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_key is not None:
            result['BusinessKey'] = self.business_key

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.elec_price_shrink is not None:
            result['ElecPrice'] = self.elec_price_shrink

        if self.freq is not None:
            result['Freq'] = self.freq

        if self.gen_price_shrink is not None:
            result['GenPrice'] = self.gen_price_shrink

        if self.location_shrink is not None:
            result['Location'] = self.location_shrink

        if self.model_version is not None:
            result['ModelVersion'] = self.model_version

        if self.run_date is not None:
            result['RunDate'] = self.run_date

        if self.system_data_shrink is not None:
            result['SystemData'] = self.system_data_shrink

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

        if m.get('ElecPrice') is not None:
            self.elec_price_shrink = m.get('ElecPrice')

        if m.get('Freq') is not None:
            self.freq = m.get('Freq')

        if m.get('GenPrice') is not None:
            self.gen_price_shrink = m.get('GenPrice')

        if m.get('Location') is not None:
            self.location_shrink = m.get('Location')

        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')

        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')

        if m.get('SystemData') is not None:
            self.system_data_shrink = m.get('SystemData')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('TopoType') is not None:
            self.topo_type = m.get('TopoType')

        return self

