# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateRulesRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class CreateRulesRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class CreateRulesRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: CreateRulesRequestHomeAddressLocation = None,
        t: CreateRulesRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = CreateRulesRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = CreateRulesRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class CreateRulesRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class CreateRulesRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HomeDMapValueLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # Lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HomeDMapValue(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HomeDMapValueLocation = None,
    ):
        # detail
        self.detail = detail
        # location
        self.location = location

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HomeDMapValueLocation()
            self.location = temp_model.from_map(m['Location'])
        return self


class CreateRulesRequestHome(TeaModel):
    def __init__(
        self,
        address: CreateRulesRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[CreateRulesRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: CreateRulesRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = CreateRulesRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = CreateRulesRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = CreateRulesRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class CreateRulesRequest(TeaModel):
    def __init__(
        self,
        home: CreateRulesRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = CreateRulesRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class CreateRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class CreateRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGrayRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGrayRequestHomeAddressLocation = None,
        t: HuichengTestGrayRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGrayRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGrayRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGrayRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGrayRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGrayRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGrayRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGrayRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGrayRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGrayRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGrayRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGrayShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGrayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGrayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGrayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGrayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGrayEightRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayEightRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayEightRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGrayEightRequestHomeAddressLocation = None,
        t: HuichengTestGrayEightRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGrayEightRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGrayEightRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayEightRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayEightRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayEightRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGrayEightRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGrayEightRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGrayEightRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGrayEightRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGrayEightRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGrayEightRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayEightRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGrayEightRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGrayEightRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGrayEightShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGrayEightResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGrayEightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGrayEightResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGrayEightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGrayFifthRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayFifthRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayFifthRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGrayFifthRequestHomeAddressLocation = None,
        t: HuichengTestGrayFifthRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGrayFifthRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGrayFifthRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayFifthRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayFifthRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayFifthRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGrayFifthRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGrayFifthRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGrayFifthRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGrayFifthRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGrayFifthRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGrayFifthRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayFifthRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGrayFifthRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGrayFifthRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGrayFifthShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGrayFifthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGrayFifthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGrayFifthResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGrayFifthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGrayFourthRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayFourthRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayFourthRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGrayFourthRequestHomeAddressLocation = None,
        t: HuichengTestGrayFourthRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGrayFourthRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGrayFourthRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayFourthRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayFourthRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayFourthRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGrayFourthRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGrayFourthRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGrayFourthRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGrayFourthRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGrayFourthRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGrayFourthRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayFourthRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGrayFourthRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGrayFourthRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGrayFourthShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGrayFourthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGrayFourthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGrayFourthResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGrayFourthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGrayNineRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayNineRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayNineRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGrayNineRequestHomeAddressLocation = None,
        t: HuichengTestGrayNineRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGrayNineRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGrayNineRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayNineRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayNineRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayNineRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGrayNineRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGrayNineRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGrayNineRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGrayNineRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGrayNineRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGrayNineRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayNineRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGrayNineRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGrayNineRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGrayNineShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGrayNineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGrayNineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGrayNineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGrayNineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGraySecondRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGraySecondRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGraySecondRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGraySecondRequestHomeAddressLocation = None,
        t: HuichengTestGraySecondRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGraySecondRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGraySecondRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGraySecondRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGraySecondRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGraySecondRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGraySecondRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGraySecondRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGraySecondRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGraySecondRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGraySecondRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGraySecondRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGraySecondRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGraySecondRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGraySecondRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGraySecondShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGraySecondResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGraySecondResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGraySecondResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGraySecondResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGraySevenRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGraySevenRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGraySevenRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGraySevenRequestHomeAddressLocation = None,
        t: HuichengTestGraySevenRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGraySevenRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGraySevenRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGraySevenRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGraySevenRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGraySevenRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGraySevenRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGraySevenRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGraySevenRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGraySevenRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGraySevenRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGraySevenRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGraySevenRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGraySevenRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGraySevenRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGraySevenShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGraySevenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGraySevenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGraySevenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGraySevenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGraySixRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGraySixRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGraySixRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGraySixRequestHomeAddressLocation = None,
        t: HuichengTestGraySixRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGraySixRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGraySixRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGraySixRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGraySixRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGraySixRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGraySixRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGraySixRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGraySixRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGraySixRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGraySixRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGraySixRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGraySixRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGraySixRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGraySixRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGraySixShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGraySixResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGraySixResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGraySixResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGraySixResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGrayTenRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayTenRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayTenRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGrayTenRequestHomeAddressLocation = None,
        t: HuichengTestGrayTenRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGrayTenRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGrayTenRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayTenRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayTenRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayTenRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGrayTenRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGrayTenRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGrayTenRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGrayTenRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGrayTenRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGrayTenRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayTenRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGrayTenRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGrayTenRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGrayTenShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGrayTenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGrayTenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGrayTenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGrayTenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestGrayThirdRequestHomeAddressLocation(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # late
        self.late = late
        # lon
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayThirdRequestHomeAddressT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayThirdRequestHomeAddress(TeaModel):
    def __init__(
        self,
        detail: str = None,
        location: HuichengTestGrayThirdRequestHomeAddressLocation = None,
        t: HuichengTestGrayThirdRequestHomeAddressT = None,
    ):
        # detail
        self.detail = detail
        # asdasd
        self.location = location
        # t
        self.t = t

    def validate(self):
        if self.location:
            self.location.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Location') is not None:
            temp_model = HuichengTestGrayThirdRequestHomeAddressLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('T') is not None:
            temp_model = HuichengTestGrayThirdRequestHomeAddressT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayThirdRequestHomeLocations(TeaModel):
    def __init__(
        self,
        late: int = None,
        lon: int = None,
    ):
        # asdasd
        self.late = late
        # sadasd
        self.lon = lon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.late is not None:
            result['Late'] = self.late
        if self.lon is not None:
            result['Lon'] = self.lon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Late') is not None:
            self.late = m.get('Late')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        return self


class HuichengTestGrayThirdRequestHomeT(TeaModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # class
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        return self


class HuichengTestGrayThirdRequestHome(TeaModel):
    def __init__(
        self,
        address: HuichengTestGrayThirdRequestHomeAddress = None,
        dmap: Dict[str, HomeDMapValue] = None,
        locations: List[HuichengTestGrayThirdRequestHomeLocations] = None,
        name_to_age: Dict[str, int] = None,
        phone_numbers: List[str] = None,
        t: HuichengTestGrayThirdRequestHomeT = None,
    ):
        # asdasd
        self.address = address
        # dMap
        self.dmap = dmap
        # asdasd
        self.locations = locations
        # NameToAge
        self.name_to_age = name_to_age
        # asdasd
        self.phone_numbers = phone_numbers
        # t
        self.t = t

    def validate(self):
        if self.address:
            self.address.validate()
        if self.dmap:
            for v in self.dmap.values():
                if v:
                    v.validate()
        if self.locations:
            for k in self.locations:
                if k:
                    k.validate()
        if self.t:
            self.t.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        result['DMap'] = {}
        if self.dmap is not None:
            for k, v in self.dmap.items():
                result['DMap'][k] = v.to_map()
        result['Locations'] = []
        if self.locations is not None:
            for k in self.locations:
                result['Locations'].append(k.to_map() if k else None)
        if self.name_to_age is not None:
            result['NameToAge'] = self.name_to_age
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.t is not None:
            result['T'] = self.t.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = HuichengTestGrayThirdRequestHomeAddress()
            self.address = temp_model.from_map(m['Address'])
        self.dmap = {}
        if m.get('DMap') is not None:
            for k, v in m.get('DMap').items():
                temp_model = HomeDMapValue()
                self.dmap[k] = temp_model.from_map(v)
        self.locations = []
        if m.get('Locations') is not None:
            for k in m.get('Locations'):
                temp_model = HuichengTestGrayThirdRequestHomeLocations()
                self.locations.append(temp_model.from_map(k))
        if m.get('NameToAge') is not None:
            self.name_to_age = m.get('NameToAge')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('T') is not None:
            temp_model = HuichengTestGrayThirdRequestHomeT()
            self.t = temp_model.from_map(m['T'])
        return self


class HuichengTestGrayThirdRequest(TeaModel):
    def __init__(
        self,
        home: HuichengTestGrayThirdRequestHome = None,
    ):
        # home
        self.home = home

    def validate(self):
        if self.home:
            self.home.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home is not None:
            result['Home'] = self.home.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            temp_model = HuichengTestGrayThirdRequestHome()
            self.home = temp_model.from_map(m['Home'])
        return self


class HuichengTestGrayThirdShrinkRequest(TeaModel):
    def __init__(
        self,
        home_shrink: str = None,
    ):
        # home
        self.home_shrink = home_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.home_shrink is not None:
            result['Home'] = self.home_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Home') is not None:
            self.home_shrink = m.get('Home')
        return self


class HuichengTestGrayThirdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        value: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # size
        self.size = size
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class HuichengTestGrayThirdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestGrayThirdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestGrayThirdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengTestResourceOwnerIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class HuichengTestResourceOwnerIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengTestResourceOwnerIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengTestResourceOwnerIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class HuichengetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HuichengetestResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class HuichengetestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HuichengetestResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HuichengetestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


