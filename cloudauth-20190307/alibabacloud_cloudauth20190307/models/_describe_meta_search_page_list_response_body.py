# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeMetaSearchPageListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeMetaSearchPageListResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The paginated list data.
        self.items = items
        # The number of entries per page.
        self.page_size = page_size
        # The ID of this request.
        self.request_id = request_id
        # The total number of pages.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeMetaSearchPageListResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeMetaSearchPageListResponseBodyItems(DaraModel):
    def __init__(
        self,
        api: str = None,
        api_name: str = None,
        bank_card: str = None,
        biz_code: str = None,
        date: str = None,
        identify_num: str = None,
        isp_name: str = None,
        mobile: str = None,
        request: main_models.DescribeMetaSearchPageListResponseBodyItemsRequest = None,
        request_id: str = None,
        request_json: str = None,
        response: main_models.DescribeMetaSearchPageListResponseBodyItemsResponse = None,
        response_json: str = None,
        sub_code: str = None,
        user_name: str = None,
        vehicle_num: str = None,
    ):
        # The product API. Valid values:
        # - **ID_CARD_2_META**: ID card two-element verification
        # - **ID_PERIOD**: ID card validity period verification
        # - **MOBILE_ONLINE_LENGTH**: mobile number online duration
        # - **MOBILE_ONLINE_STATUS**: mobile number online status
        # - **MOBILE_3_META_SIMPLE**: mobile number three-element verification (simple edition)
        # - **MOBILE_3_META**: mobile number three-element verification (detailed edition)
        # - **MOBILE_2_META**: mobile number two-element verification
        # - **BANK_CARD_N_META**: bank card verification (detailed edition)
        # - **MOBILE_DETECT**: phone number detection 
        # - **VEHICLE_N_META**: vehicle element verification (enhanced edition)
        # - **VEHICLE_PENTA_INFO**: vehicle five-element information recognition
        # - **VEHICLE_LICENSE_INFO**: vehicle information recognition
        # - **VEHICLE_INSURE_DATE**: vehicle insurance date query
        # - **VEHICLE_CHECK**: vehicle element verification.
        self.api = api
        # The name corresponding to the API. Valid values:
        # - **ID_CARD_2_META**: ID card two-element verification
        # - **ID_PERIOD**: ID card validity period verification
        # - **MOBILE_ONLINE_LENGTH**: mobile number online duration
        # - **MOBILE_ONLINE_STATUS**: mobile number online status
        # - **MOBILE_3_META_SIMPLE**: mobile number three-element verification (simple edition)
        # - **MOBILE_3_META**: mobile number three-element verification (detailed edition)
        # - **MOBILE_2_META**: mobile number two-element verification
        # - **BANK_CARD_N_META**: bank card verification (detailed edition)
        # - **MOBILE_DETECT**: phone number detection 
        # - **VEHICLE_N_META**: vehicle element verification (enhanced edition)
        # - **VEHICLE_PENTA_INFO**: vehicle five-element information recognition
        # - **VEHICLE_LICENSE_INFO**: vehicle information recognition
        # - **VEHICLE_INSURE_DATE**: vehicle insurance date query
        # - **VEHICLE_CHECK**: vehicle element verification.
        self.api_name = api_name
        # The bank card ID.
        self.bank_card = bank_card
        # The verification status. Valid values:
        # - **1**: Verification passed.
        # - **2**: Verification failed.
        # - **3**: No record found.
        self.biz_code = biz_code
        # The verification date.
        self.date = date
        # The ID card number.
        self.identify_num = identify_num
        # The name of the telecommunications service provider. Valid values:
        # - **CMCC**: China Mobile
        # - **CUCC**: China Unicom
        # - **CTCC**: China Telecom.
        self.isp_name = isp_name
        # The mobile phone number.
        self.mobile = mobile
        # The request parameters.
        self.request = request
        # The request ID.
        self.request_id = request_id
        # The HTTP request parameters.
        self.request_json = request_json
        # The response content.
        self.response = response
        # The response content.
        self.response_json = response_json
        # The result code. For more information, see [official documentation](https://www.alibabacloud.com/help/en/id-verification/information-verification/).
        self.sub_code = sub_code
        # The name.
        self.user_name = user_name
        # The vehicle number.
        self.vehicle_num = vehicle_num

    def validate(self):
        if self.request:
            self.request.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api is not None:
            result['Api'] = self.api

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.bank_card is not None:
            result['BankCard'] = self.bank_card

        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.date is not None:
            result['Date'] = self.date

        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.request is not None:
            result['Request'] = self.request.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_json is not None:
            result['RequestJson'] = self.request_json

        if self.response is not None:
            result['Response'] = self.response.to_map()

        if self.response_json is not None:
            result['ResponseJson'] = self.response_json

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('BankCard') is not None:
            self.bank_card = m.get('BankCard')

        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Request') is not None:
            temp_model = main_models.DescribeMetaSearchPageListResponseBodyItemsRequest()
            self.request = temp_model.from_map(m.get('Request'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestJson') is not None:
            self.request_json = m.get('RequestJson')

        if m.get('Response') is not None:
            temp_model = main_models.DescribeMetaSearchPageListResponseBodyItemsResponse()
            self.response = temp_model.from_map(m.get('Response'))

        if m.get('ResponseJson') is not None:
            self.response_json = m.get('ResponseJson')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')

        return self

class DescribeMetaSearchPageListResponseBodyItemsResponse(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeMetaSearchPageListResponseBodyItemsResponseData = None,
        message: str = None,
    ):
        # The HTTP return code.
        self.code = code
        # The response data.
        self.data = data
        # The message.
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeMetaSearchPageListResponseBodyItemsResponseData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class DescribeMetaSearchPageListResponseBodyItemsResponseData(DaraModel):
    def __init__(
        self,
        approved_count: str = None,
        approved_load: str = None,
        axle_count: str = None,
        back_wheel_distance: str = None,
        bank_card: str = None,
        biz_code: str = None,
        brand: str = None,
        color: str = None,
        displacement: str = None,
        engine_num: str = None,
        engine_type: str = None,
        front_wheel_distance: str = None,
        fuel_type: str = None,
        inspection_date: str = None,
        model_num: str = None,
        power: str = None,
        registration_date: str = None,
        release_date: str = None,
        retirement_date: str = None,
        total_mass: str = None,
        type: str = None,
        unladen_mass: str = None,
        use_property: str = None,
        vehicle_state: str = None,
        vin: str = None,
        wheel_base: str = None,
    ):
        # The approved number of passengers.
        self.approved_count = approved_count
        # The approved passenger capacity.
        self.approved_load = approved_load
        # The number of axles.
        self.axle_count = axle_count
        # The rear wheel track.
        self.back_wheel_distance = back_wheel_distance
        # The bank card number.
        self.bank_card = bank_card
        # The verification status. Valid values:
        # - **1**: Verification passed.
        # - **2**: Verification failed.
        # - **3**: No record found.
        self.biz_code = biz_code
        # The brand name.
        self.brand = brand
        # The body color.
        self.color = color
        # The displacement.
        self.displacement = displacement
        # The engine number.
        self.engine_num = engine_num
        # The engine model.
        self.engine_type = engine_type
        # The front wheel track.
        self.front_wheel_distance = front_wheel_distance
        # The fuel type.
        self.fuel_type = fuel_type
        # The inspection validity expiration date.
        self.inspection_date = inspection_date
        # The vehicle model number.
        self.model_num = model_num
        # The power.
        self.power = power
        # The initial registration date.
        self.registration_date = registration_date
        # The manufacturing date.
        self.release_date = release_date
        # The mandatory retirement date.
        self.retirement_date = retirement_date
        # The gross mass.
        self.total_mass = total_mass
        # The vehicle type.
        self.type = type
        # The curb weight.
        self.unladen_mass = unladen_mass
        # The usage property.
        self.use_property = use_property
        # The motor vehicle status.
        self.vehicle_state = vehicle_state
        # The vehicle identification number (VIN).
        self.vin = vin
        # The wheelbase.
        self.wheel_base = wheel_base

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approved_count is not None:
            result['ApprovedCount'] = self.approved_count

        if self.approved_load is not None:
            result['ApprovedLoad'] = self.approved_load

        if self.axle_count is not None:
            result['AxleCount'] = self.axle_count

        if self.back_wheel_distance is not None:
            result['BackWheelDistance'] = self.back_wheel_distance

        if self.bank_card is not None:
            result['BankCard'] = self.bank_card

        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.brand is not None:
            result['Brand'] = self.brand

        if self.color is not None:
            result['Color'] = self.color

        if self.displacement is not None:
            result['Displacement'] = self.displacement

        if self.engine_num is not None:
            result['EngineNum'] = self.engine_num

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.front_wheel_distance is not None:
            result['FrontWheelDistance'] = self.front_wheel_distance

        if self.fuel_type is not None:
            result['FuelType'] = self.fuel_type

        if self.inspection_date is not None:
            result['InspectionDate'] = self.inspection_date

        if self.model_num is not None:
            result['ModelNum'] = self.model_num

        if self.power is not None:
            result['Power'] = self.power

        if self.registration_date is not None:
            result['RegistrationDate'] = self.registration_date

        if self.release_date is not None:
            result['ReleaseDate'] = self.release_date

        if self.retirement_date is not None:
            result['RetirementDate'] = self.retirement_date

        if self.total_mass is not None:
            result['TotalMass'] = self.total_mass

        if self.type is not None:
            result['Type'] = self.type

        if self.unladen_mass is not None:
            result['UnladenMass'] = self.unladen_mass

        if self.use_property is not None:
            result['UseProperty'] = self.use_property

        if self.vehicle_state is not None:
            result['VehicleState'] = self.vehicle_state

        if self.vin is not None:
            result['Vin'] = self.vin

        if self.wheel_base is not None:
            result['WheelBase'] = self.wheel_base

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovedCount') is not None:
            self.approved_count = m.get('ApprovedCount')

        if m.get('ApprovedLoad') is not None:
            self.approved_load = m.get('ApprovedLoad')

        if m.get('AxleCount') is not None:
            self.axle_count = m.get('AxleCount')

        if m.get('BackWheelDistance') is not None:
            self.back_wheel_distance = m.get('BackWheelDistance')

        if m.get('BankCard') is not None:
            self.bank_card = m.get('BankCard')

        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('Displacement') is not None:
            self.displacement = m.get('Displacement')

        if m.get('EngineNum') is not None:
            self.engine_num = m.get('EngineNum')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('FrontWheelDistance') is not None:
            self.front_wheel_distance = m.get('FrontWheelDistance')

        if m.get('FuelType') is not None:
            self.fuel_type = m.get('FuelType')

        if m.get('InspectionDate') is not None:
            self.inspection_date = m.get('InspectionDate')

        if m.get('ModelNum') is not None:
            self.model_num = m.get('ModelNum')

        if m.get('Power') is not None:
            self.power = m.get('Power')

        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')

        if m.get('ReleaseDate') is not None:
            self.release_date = m.get('ReleaseDate')

        if m.get('RetirementDate') is not None:
            self.retirement_date = m.get('RetirementDate')

        if m.get('TotalMass') is not None:
            self.total_mass = m.get('TotalMass')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UnladenMass') is not None:
            self.unladen_mass = m.get('UnladenMass')

        if m.get('UseProperty') is not None:
            self.use_property = m.get('UseProperty')

        if m.get('VehicleState') is not None:
            self.vehicle_state = m.get('VehicleState')

        if m.get('Vin') is not None:
            self.vin = m.get('Vin')

        if m.get('WheelBase') is not None:
            self.wheel_base = m.get('WheelBase')

        return self

class DescribeMetaSearchPageListResponseBodyItemsRequest(DaraModel):
    def __init__(
        self,
        vehicle_num: str = None,
        vehicle_type: str = None,
        vehicle_type_name: str = None,
    ):
        # The vehicle number.
        self.vehicle_num = vehicle_num
        # The vehicle type. Valid values:
        # - **01**: large vehicle  
        # - **02**: small vehicle  
        # - **03**: embassy vehicle  
        # - **04**: consulate vehicle  
        # - **05**: overseas vehicle  
        # - **06**: foreign vehicle  
        # - **07**: standard motorcycle  
        # - **08**: light motorcycle  
        # - **09**: embassy motorcycle  
        # - **10**: consulate motorcycle  
        # - **11**: overseas motorcycle  
        # - **12**: foreign motorcycle  
        # - **13**: low-speed vehicle  
        # - **14**: tractor  
        # - **15**: trailer  
        # - **16**: training vehicle  
        # - **17**: training motorcycle  
        # - **20**: temporary entry vehicle  
        # - **21**: temporary entry motorcycle  
        # - **22**: temporary driving vehicle  
        # - **23**: police vehicle  
        # - **24**: police motorcycle  
        # - **51**: new energy large vehicle  
        # - **52**: new energy small vehicle.
        self.vehicle_type = vehicle_type
        # The vehicle type name.
        self.vehicle_type_name = vehicle_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num

        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type

        if self.vehicle_type_name is not None:
            result['VehicleTypeName'] = self.vehicle_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')

        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')

        if m.get('VehicleTypeName') is not None:
            self.vehicle_type_name = m.get('VehicleTypeName')

        return self

