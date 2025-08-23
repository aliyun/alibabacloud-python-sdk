# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, BinaryIO


class AddressCompareIntlRequest(TeaModel):
    def __init__(
        self,
        default_country: str = None,
        product_code: str = None,
        text_1: str = None,
        text_2: str = None,
    ):
        # This parameter is required.
        self.default_country = default_country
        # ADD_VERIFY
        # 
        # This parameter is required.
        self.product_code = product_code
        # This parameter is required.
        self.text_1 = text_1
        # This parameter is required.
        self.text_2 = text_2

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_country is not None:
            result['DefaultCountry'] = self.default_country
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.text_1 is not None:
            result['Text1'] = self.text_1
        if self.text_2 is not None:
            result['Text2'] = self.text_2
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCountry') is not None:
            self.default_country = m.get('DefaultCountry')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Text1') is not None:
            self.text_1 = m.get('Text1')
        if m.get('Text2') is not None:
            self.text_2 = m.get('Text2')
        return self


class AddressCompareIntlResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class AddressCompareIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: AddressCompareIntlResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddressCompareIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class AddressCompareIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddressCompareIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddressCompareIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddressVerifyIntlRequest(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        default_city: str = None,
        default_country: str = None,
        default_district: str = None,
        default_province: str = None,
        latitude: str = None,
        longitude: str = None,
        mobile: str = None,
        product_code: str = None,
        text: str = None,
        verify_type: str = None,
    ):
        # Verification address type:
        # - “0”: Text address
        # - “1”: Latitude and longitude
        # 
        # This parameter is required.
        self.address_type = address_type
        # Default city
        self.default_city = default_city
        # Country name, currently only supports: China
        # 
        # This parameter is required.
        self.default_country = default_country
        # Default district
        self.default_district = default_district
        # Default province
        self.default_province = default_province
        # Latitude.
        self.latitude = latitude
        # Longitude.
        self.longitude = longitude
        # Supports Chinese mobile phone numbers.
        # 
        # This parameter is required.
        self.mobile = mobile
        # Fixed value: ADD_VERIFY_PRO
        # 
        # This parameter is required.
        self.product_code = product_code
        # Detailed address text content
        self.text = text
        # Address verification method:
        # - HOME: Home address verification
        # - WORK: Work address verification
        # 
        # This parameter is required.
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_country is not None:
            result['DefaultCountry'] = self.default_country
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.text is not None:
            result['Text'] = self.text
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultCountry') is not None:
            self.default_country = m.get('DefaultCountry')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class AddressVerifyIntlResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        address_info: str = None,
        isp_name: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        # Address verification details.
        self.address_info = address_info
        # Operator name:
        # - CMCC: China Mobile
        # - CTCC: China Telecom
        # - CUCC: China Unicom
        self.isp_name = isp_name
        # Verification result, values:
        # - Y: Yes, the verified address distance is less than or equal to 10KM.
        # - N: No, the verified address distance is greater than 10KM.
        self.passed = passed
        # Authentication result description.
        self.sub_code = sub_code
        # Unique identifier for the authentication request.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressInfo') is not None:
            self.address_info = m.get('AddressInfo')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class AddressVerifyIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: AddressVerifyIntlResponseBodyResultObject = None,
    ):
        # Return code.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = AddressVerifyIntlResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class AddressVerifyIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddressVerifyIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddressVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddressVerifyV2IntlRequest(TeaModel):
    def __init__(
        self,
        device_token: str = None,
        mobile: str = None,
        product_code: str = None,
        reg_country: str = None,
        text: str = None,
        verify_type: str = None,
    ):
        # This parameter is required.
        self.device_token = device_token
        self.mobile = mobile
        # This parameter is required.
        self.product_code = product_code
        # This parameter is required.
        self.reg_country = reg_country
        self.text = text
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reg_country is not None:
            result['RegCountry'] = self.reg_country
        if self.text is not None:
            result['Text'] = self.text
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegCountry') is not None:
            self.reg_country = m.get('RegCountry')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class AddressVerifyV2IntlResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        detail: str = None,
        transaction_id: str = None,
    ):
        self.biz_code = biz_code
        self.detail = detail
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class AddressVerifyV2IntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: AddressVerifyV2IntlResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddressVerifyV2IntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class AddressVerifyV2IntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddressVerifyV2IntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddressVerifyV2IntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BankMetaVerifyIntlRequest(TeaModel):
    def __init__(
        self,
        bank_card: str = None,
        identify_num: str = None,
        identity_type: str = None,
        mobile: str = None,
        param_type: str = None,
        product_code: str = None,
        product_type: str = None,
        user_name: str = None,
        verify_mode: str = None,
    ):
        # Bank card number.
        # 
        # - When paramType is set to normal, enter the plaintext bank card number.
        # - When paramType is set to md5, enter the plaintext part of the card number except the last 6 digits, followed by the MD5 value of the last 6 digits (32-character lowercase).
        # 
        # This parameter is required.
        self.bank_card = bank_card
        # ID number:
        # - When paramType is normal: Enter the plaintext ID number.
        # - When paramType is md5:
        #     - First 6 digits of the ID number (plaintext) + date of birth (ciphertext) + last 4 digits of the ID number (plaintext).
        #     - For other IDs, encrypt the last two digits with MD5.
        # 
        # Important
        # This field is required when ProductType is one of the following:
        # - BANK_CARD_3_META
        # - BANK_CARD_4_META
        self.identify_num = identify_num
        # ID type (default to ID card if left empty, see the table below for other types).
        self.identity_type = identity_type
        # Phone number:
        # - When paramType is normal: Enter the plaintext phone number.
        # - When paramType is md5: Enter the ciphertext phone number.
        # 
        # Important
        # 
        # - This field is required when ProductType = BANK_CARD_4_META.
        self.mobile = mobile
        # Encryption method:
        # - normal: no encryption
        # - md5: md5 encryption
        # 
        # Important:
        # 
        # - All encrypted parameters should be in the form of a 32-character lowercase MD5 string.
        # - The ciphertext generated by different MD5 tools may vary. If the interface works before encryption but not after, try changing the MD5 tool.
        # 
        # This parameter is required.
        self.param_type = param_type
        # Fixed value: BANK_CARD_N_META
        # 
        # This parameter is required.
        self.product_code = product_code
        # Product type to call:
        # 
        # - BANK_CARD_2_META: Bank card number + name verification.
        # - BANK_CARD_3_META: Bank card number + name + ID number verification.
        # - BANK_CARD_4_META: Bank card number + name + ID number + phone number verification.
        # 
        # This parameter is required.
        self.product_type = product_type
        # Name.
        # 
        # - When paramType is set to normal, enter the plaintext name.
        # - When paramType is set to md5, encrypt the first character of the name with MD5 (32-character lowercase MD5) and append the rest of the name in plaintext.
        # 
        # This parameter is required.
        self.user_name = user_name
        # VERIFY_BANK_CARD: Bank card authentication mode. This indicates whether the provided bank card number matches the user\\"s real name, ID number, and phone number.
        # 
        # This parameter is required.
        self.verify_mode = verify_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bank_card is not None:
            result['BankCard'] = self.bank_card
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.verify_mode is not None:
            result['VerifyMode'] = self.verify_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BankCard') is not None:
            self.bank_card = m.get('BankCard')
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VerifyMode') is not None:
            self.verify_mode = m.get('VerifyMode')
        return self


class BankMetaVerifyIntlResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        sub_code: str = None,
    ):
        # Verification result code.
        # - 1: Consistent (charged)
        # - 2: Inconsistent (charged)
        # - 3: No record found (not charged)
        self.biz_code = biz_code
        # Verification details:
        # 
        # - **101**: Verification passed.
        # - **201**: Authentication information does not match, cardholder information is incorrect.
        # - **202**: Authentication information does not match, bank card has not been activated for authenticated payments.
        # - **203**: Authentication information does not match, bank card has expired.
        # - **204**: Authentication information does not match, bank card is a restricted card.
        # - **205**: Authentication information does not match, this card has been confiscated.
        # - **206**: Authentication information does not match, bank card is invalid.
        # - **207**: Authentication information does not match, this card has no corresponding issuing bank.
        # - **208**: Authentication information does not match, this card is uninitialized or dormant.
        # - **209**: Authentication information does not match, this card is a cheating card or swallowed card.
        # - **210**: Authentication information does not match, this card has been reported lost.
        # - **211**: Authentication information does not match, password error limit exceeded.
        # - **212**: Authentication information does not match, issuing bank does not support this transaction.
        # - **213**: Authentication information does not match, card status is abnormal or card is invalid.
        # - **214**: Authentication information does not match, no phone number reserved.
        # - **215**: Authentication information does not match, entered password, expiration date, or CVN2 is incorrect.
        # - **216**: Authentication information does not match, other card anomalies.
        # - **301**: Unable to verify, bank card does not support this service.
        # - **302**: Unable to verify, verification failed or bank refused verification, please contact the issuing bank.
        # - **303**: Unable to verify, bank card does not currently support phone number verification.
        # - **304**: Unable to verify, bank card number is incorrect.
        # - **305**: Unable to verify, other reasons.
        # - **306**: Unable to verify, verification attempt limit exceeded.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class BankMetaVerifyIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: BankMetaVerifyIntlResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = BankMetaVerifyIntlResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class BankMetaVerifyIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BankMetaVerifyIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BankMetaVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CardOcrRequest(TeaModel):
    def __init__(
        self,
        doc_type: str = None,
        id_face_quality: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_url: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        ocr: str = None,
        product_code: str = None,
        spoof: str = None,
    ):
        # Document type.
        self.doc_type = doc_type
        # Whether to perform face quality detection on the document
        # - T: Indicates that detection is needed
        # - F: Indicates that detection is not needed (default F)
        self.id_face_quality = id_face_quality
        # Base64 on the front of the document image
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        # URL of the front side of the document image
        self.id_ocr_picture_url = id_ocr_picture_url
        # A unique business identifier defined by the merchant, used for subsequent troubleshooting. It supports a combination of letters and numbers, with a maximum length of 32 characters. Please ensure uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # Merchant user ID or other identifiers that can be used to identify specific users, such as phone numbers, email addresses, etc. It is strongly recommended to pre-desensitize the value of the userId field, for example, by hashing the value.
        self.merchant_user_id = merchant_user_id
        # Whether to perform document OCR
        # - T: Indicates that document OCR is required (default T)
        # - F: Indicates that it is not required
        self.ocr = ocr
        # Product code
        self.product_code = product_code
        # Whether to enable anti-counterfeiting detection
        # - T: Indicates to enable anti-counterfeiting
        # - F: Indicates to disable (default F)
        self.spoof = spoof

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.spoof is not None:
            result['Spoof'] = self.spoof
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Spoof') is not None:
            self.spoof = m.get('Spoof')
        return self


class CardOcrResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_card_info: str = None,
        ext_id_info: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        # Document recognition result
        self.ext_card_info = ext_card_info
        # Additional result information
        self.ext_id_info = ext_id_info
        # Whether the authentication passed.
        # 
        # - Y: Passed.
        # - N: Not passed.
        self.passed = passed
        # Sub-result code.
        self.sub_code = sub_code
        # Unique identifier for the authentication request
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_card_info is not None:
            result['ExtCardInfo'] = self.ext_card_info
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtCardInfo') is not None:
            self.ext_card_info = m.get('ExtCardInfo')
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class CardOcrResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CardOcrResponseBodyResult = None,
    ):
        # Return code
        self.code = code
        # Return message
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Return result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CardOcrResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CardOcrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CardOcrResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CardOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckResultRequest(TeaModel):
    def __init__(
        self,
        extra_image_control_list: str = None,
        is_return_image: str = None,
        merchant_biz_id: str = None,
        return_five_category_spoof_result: str = None,
        transaction_id: str = None,
    ):
        # Return additional information.
        self.extra_image_control_list = extra_image_control_list
        # Whether to return images.
        # - Y: Return
        # - N: Do not return
        self.is_return_image = is_return_image
        # A unique business identifier defined by the merchant, used for subsequent troubleshooting. It supports a combination of letters and numbers, with a maximum length of 32 characters. Please ensure its uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # Whether to return anti-fraud detection results.
        self.return_five_category_spoof_result = return_five_category_spoof_result
        # Authentication ID.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_image_control_list is not None:
            result['ExtraImageControlList'] = self.extra_image_control_list
        if self.is_return_image is not None:
            result['IsReturnImage'] = self.is_return_image
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.return_five_category_spoof_result is not None:
            result['ReturnFiveCategorySpoofResult'] = self.return_five_category_spoof_result
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraImageControlList') is not None:
            self.extra_image_control_list = m.get('ExtraImageControlList')
        if m.get('IsReturnImage') is not None:
            self.is_return_image = m.get('IsReturnImage')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('ReturnFiveCategorySpoofResult') is not None:
            self.return_five_category_spoof_result = m.get('ReturnFiveCategorySpoofResult')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class CheckResultResponseBodyResult(TeaModel):
    def __init__(
        self,
        ekyc_result: str = None,
        ext_basic_info: str = None,
        ext_face_info: str = None,
        ext_id_info: str = None,
        ext_info: str = None,
        ext_risk_info: str = None,
        passed: str = None,
        sub_code: str = None,
    ):
        # Authentication result.
        self.ekyc_result = ekyc_result
        # Extended basic information.
        self.ext_basic_info = ext_basic_info
        # Face information.
        self.ext_face_info = ext_face_info
        # ID information.
        self.ext_id_info = ext_id_info
        # Extended information
        self.ext_info = ext_info
        # Risk information.
        self.ext_risk_info = ext_risk_info
        # Whether the authentication is passed.
        # 
        # - Y: Passed
        # - N: Not passed
        self.passed = passed
        # Sub-result code.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ekyc_result is not None:
            result['EkycResult'] = self.ekyc_result
        if self.ext_basic_info is not None:
            result['ExtBasicInfo'] = self.ext_basic_info
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.ext_risk_info is not None:
            result['ExtRiskInfo'] = self.ext_risk_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EkycResult') is not None:
            self.ekyc_result = m.get('EkycResult')
        if m.get('ExtBasicInfo') is not None:
            self.ext_basic_info = m.get('ExtBasicInfo')
        if m.get('ExtFaceInfo') is not None:
            self.ext_face_info = m.get('ExtFaceInfo')
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('ExtRiskInfo') is not None:
            self.ext_risk_info = m.get('ExtRiskInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class CheckResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CheckResultResponseBodyResult = None,
    ):
        # Return code.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Return result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CheckResultResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckVerifyLogRequest(TeaModel):
    def __init__(
        self,
        merchant_biz_id: str = None,
        transaction_id: str = None,
    ):
        # A unique business identifier defined by the merchant, used for subsequent problem localization and troubleshooting. Supports a combination of letters and numbers, with a maximum length of 32 characters. Ensure uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # The unique identifier for the entire authentication process. This value needs to be obtained by calling Initialize.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class CheckVerifyLogResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_info: str = None,
        interrupt_page: str = None,
        interrupt_page_en: str = None,
        log_info: List[str] = None,
        log_info_en: List[str] = None,
        log_statistics_info: str = None,
        passed: str = None,
        sub_code: str = None,
        verify_error_code: str = None,
        verify_status: str = None,
    ):
        # Extended information
        self.ext_info = ext_info
        # Records the last page where the authentication was interrupted.
        # 
        # - Page not started
        # - OCR guide page
        # - OCR camera authorization
        # - OCR document capture page
        # - OCR recognition loading
        # - OCR recognition result editing page
        # - OCR recognition result editing loading
        # - Liveness detection guide page
        # - Liveness detection camera authorization page
        # - Liveness detection page
        # - Liveness detection fallback page
        # - Liveness detection retry
        # - Liveness detection loading
        self.interrupt_page = interrupt_page
        self.interrupt_page_en = interrupt_page_en
        # SDK operation log details
        self.log_info = log_info
        self.log_info_en = log_info_en
        # SDK operation log statistics details
        self.log_statistics_info = log_statistics_info
        # Whether the authentication passed.
        # 
        # - Y: Passed.
        # - N: Not passed.
        self.passed = passed
        # Sub-result code
        self.sub_code = sub_code
        # Authentication interruption error codes
        # 
        # - 1000: The user completed the face scanning process, and the suggested authentication result is pass
        # - 1001: The user completed the face scanning process, and the suggested authentication result is fail
        # - 1002: System error
        # - 1003: SDK initialization failed, please check if the client time is correct
        # - 1004: Camera permission error
        # - 1005: Network error
        # - 1006: User exited
        # - 1007: Invalid TransactionId
        # - 1009: Client timestamp error
        # - 1011: Incorrect document type submitted
        # - 1012: Missing or format validation failure of key information on the recognized document
        # - 1013: Poor image quality
        # - 1014: Exceeded the upper limit of errors
        # - 1015: Android system version too low
        # - 1016: Camera permission not obtained
        # - 9999: Suspected authentication process interruption
        self.verify_error_code = verify_error_code
        # Authentication status, values:
        # 
        # - 0: finished (authentication completed)
        # - 1: unfinished (authentication interrupted)
        # - 2: notstart (authentication not started)
        self.verify_status = verify_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.interrupt_page is not None:
            result['InterruptPage'] = self.interrupt_page
        if self.interrupt_page_en is not None:
            result['InterruptPageEn'] = self.interrupt_page_en
        if self.log_info is not None:
            result['LogInfo'] = self.log_info
        if self.log_info_en is not None:
            result['LogInfoEn'] = self.log_info_en
        if self.log_statistics_info is not None:
            result['LogStatisticsInfo'] = self.log_statistics_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.verify_error_code is not None:
            result['VerifyErrorCode'] = self.verify_error_code
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('InterruptPage') is not None:
            self.interrupt_page = m.get('InterruptPage')
        if m.get('InterruptPageEn') is not None:
            self.interrupt_page_en = m.get('InterruptPageEn')
        if m.get('LogInfo') is not None:
            self.log_info = m.get('LogInfo')
        if m.get('LogInfoEn') is not None:
            self.log_info_en = m.get('LogInfoEn')
        if m.get('LogStatisticsInfo') is not None:
            self.log_statistics_info = m.get('LogStatisticsInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('VerifyErrorCode') is not None:
            self.verify_error_code = m.get('VerifyErrorCode')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        return self


class CheckVerifyLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CheckVerifyLogResponseBodyResult = None,
    ):
        # Backend error code.
        self.code = code
        # Return message
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Return result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CheckVerifyLogResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckVerifyLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckVerifyLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckVerifyLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CredentialVerifyIntlRequest(TeaModel):
    def __init__(
        self,
        cred_name: str = None,
        cred_type: str = None,
        image_file: str = None,
        image_url: str = None,
        product_code: str = None,
    ):
        # Credential name (numeric code):
        # 
        # - Starting with 03: Enterprise Qualification
        #   - 0301: Mainland China Business License
        # - Starting with 04, Transaction Voucher
        #   - 0401: Bank Statement
        #   - 0402: Pay Slip
        #   - 0403: Utility Bill
        #   - 0405: Credit Card Statement
        #   - 0499: Others
        # 
        # This parameter is required.
        self.cred_name = cred_name
        # Credential type:
        # 
        # - 03: Enterprise Qualification
        # - 04: Transaction Voucher
        # 
        # This parameter is required.
        self.cred_type = cred_type
        # Image input stream.
        # > Choose either ImageUrl or ImageFile.
        self.image_file = image_file
        # The URL of the image.
        # > Choose either ImageUrl or ImageFile.
        self.image_url = image_url
        # Invocation mode:
        # - ANTI_FAKE_CHECK: Image quality and tampering detection.
        # 
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cred_name is not None:
            result['CredName'] = self.cred_name
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        if self.image_file is not None:
            result['ImageFile'] = self.image_file
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        if m.get('ImageFile') is not None:
            self.image_file = m.get('ImageFile')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class CredentialVerifyIntlAdvanceRequest(TeaModel):
    def __init__(
        self,
        cred_name: str = None,
        cred_type: str = None,
        image_file_object: BinaryIO = None,
        image_url: str = None,
        product_code: str = None,
    ):
        # Credential name (numeric code):
        # 
        # - Starting with 03: Enterprise Qualification
        #   - 0301: Mainland China Business License
        # - Starting with 04, Transaction Voucher
        #   - 0401: Bank Statement
        #   - 0402: Pay Slip
        #   - 0403: Utility Bill
        #   - 0405: Credit Card Statement
        #   - 0499: Others
        # 
        # This parameter is required.
        self.cred_name = cred_name
        # Credential type:
        # 
        # - 03: Enterprise Qualification
        # - 04: Transaction Voucher
        # 
        # This parameter is required.
        self.cred_type = cred_type
        # Image input stream.
        # > Choose either ImageUrl or ImageFile.
        self.image_file_object = image_file_object
        # The URL of the image.
        # > Choose either ImageUrl or ImageFile.
        self.image_url = image_url
        # Invocation mode:
        # - ANTI_FAKE_CHECK: Image quality and tampering detection.
        # 
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cred_name is not None:
            result['CredName'] = self.cred_name
        if self.cred_type is not None:
            result['CredType'] = self.cred_type
        if self.image_file_object is not None:
            result['ImageFile'] = self.image_file_object
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')
        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')
        if m.get('ImageFile') is not None:
            self.image_file_object = m.get('ImageFile')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class CredentialVerifyIntlResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        material_info: str = None,
        result: str = None,
        risk_score: Dict[str, str] = None,
        risk_tag: str = None,
    ):
        # Other information in JSON format.
        self.material_info = material_info
        # Risk result:
        # 
        # - **0**: Low risk
        # - **1**: High risk
        # - **2**: Suspicious
        self.result = result
        # Risk score map
        self.risk_score = risk_score
        # Risk tags, separated by commas (,). Includes:
        # 
        # - PS: Image manipulation (Photoshop)
        # - SCREEN_PHOTO: Screen recapture
        # - SCREENSHOT: Screenshot
        # - ORIGINAL_PHOTO: Not original image
        self.risk_tag = risk_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.result is not None:
            result['Result'] = self.result
        if self.risk_score is not None:
            result['RiskScore'] = self.risk_score
        if self.risk_tag is not None:
            result['RiskTag'] = self.risk_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RiskScore') is not None:
            self.risk_score = m.get('RiskScore')
        if m.get('RiskTag') is not None:
            self.risk_tag = m.get('RiskTag')
        return self


class CredentialVerifyIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: CredentialVerifyIntlResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = CredentialVerifyIntlResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class CredentialVerifyIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CredentialVerifyIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CredentialVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeepfakeDetectIntlRequest(TeaModel):
    def __init__(
        self,
        face_base_64: str = None,
        face_input_type: str = None,
        face_url: str = None,
        merchant_biz_id: str = None,
        product_code: str = None,
        scene_code: str = None,
    ):
        self.face_base_64 = face_base_64
        self.face_input_type = face_input_type
        self.face_url = face_url
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # This parameter is required.
        self.product_code = product_code
        self.scene_code = scene_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_base_64 is not None:
            result['FaceBase64'] = self.face_base_64
        if self.face_input_type is not None:
            result['FaceInputType'] = self.face_input_type
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceBase64') is not None:
            self.face_base_64 = m.get('FaceBase64')
        if m.get('FaceInputType') is not None:
            self.face_input_type = m.get('FaceInputType')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        return self


class DeepfakeDetectIntlResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        result: str = None,
        risk_score: Dict[str, str] = None,
        risk_tag: str = None,
    ):
        self.result = result
        self.risk_score = risk_score
        self.risk_tag = risk_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.risk_score is not None:
            result['RiskScore'] = self.risk_score
        if self.risk_tag is not None:
            result['RiskTag'] = self.risk_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RiskScore') is not None:
            self.risk_score = m.get('RiskScore')
        if m.get('RiskTag') is not None:
            self.risk_tag = m.get('RiskTag')
        return self


class DeepfakeDetectIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DeepfakeDetectIntlResponseBodyResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = DeepfakeDetectIntlResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DeepfakeDetectIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeepfakeDetectIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeepfakeDetectIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVerifyResultRequest(TeaModel):
    def __init__(
        self,
        delete_after_query: str = None,
        delete_type: str = None,
        transaction_id: str = None,
    ):
        # Whether to depend on the query interface when deleting data
        self.delete_after_query = delete_after_query
        # Type of data to be deleted
        self.delete_type = delete_type
        # Unique identifier of the authentication request
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_after_query is not None:
            result['DeleteAfterQuery'] = self.delete_after_query
        if self.delete_type is not None:
            result['DeleteType'] = self.delete_type
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAfterQuery') is not None:
            self.delete_after_query = m.get('DeleteAfterQuery')
        if m.get('DeleteType') is not None:
            self.delete_type = m.get('DeleteType')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeleteVerifyResultResponseBodyResult(TeaModel):
    def __init__(
        self,
        delete_result: str = None,
        transaction_id: str = None,
    ):
        # Deletion result. Y indicates successful deletion, N indicates failed deletion
        self.delete_result = delete_result
        # Unique identifier of the authentication request
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteResult') is not None:
            self.delete_result = m.get('DeleteResult')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeleteVerifyResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DeleteVerifyResultResponseBodyResult = None,
    ):
        # Return code
        self.code = code
        # Return message
        self.message = message
        # ID of this request
        self.request_id = request_id
        # Return result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteVerifyResultResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteVerifyResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVerifyResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteVerifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DocOcrRequest(TeaModel):
    def __init__(
        self,
        card_side: str = None,
        doc_type: str = None,
        id_face_quality: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_url: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        ocr: str = None,
        product_code: str = None,
        spoof: str = None,
    ):
        # CardSide
        self.card_side = card_side
        # Document type
        self.doc_type = doc_type
        # Whether to perform ID face quality detection
        # - T: Indicates that detection is required
        # - F: Indicates that detection is not required (default F)
        self.id_face_quality = id_face_quality
        # Base64 of the front side of the document image
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        # URL of the front side of the document image
        self.id_ocr_picture_url = id_ocr_picture_url
        # IdThreshold
        self.id_threshold = id_threshold
        # A unique business identifier defined by the merchant, used for subsequent troubleshooting. It supports a combination of letters and numbers, with a maximum length of 32 characters. Please ensure uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # A custom user ID in the business, please keep it unique.
        self.merchant_user_id = merchant_user_id
        # Whether to perform document OCR
        # - T: Indicates that document OCR is required
        # - F: Indicates that document OCR is not required
        self.ocr = ocr
        # Product code
        self.product_code = product_code
        # Whether to enable anti-counterfeiting detection
        # - T: Indicates that anti-counterfeiting is enabled
        # - F: Indicates that anti-counterfeiting is disabled
        self.spoof = spoof

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_side is not None:
            result['CardSide'] = self.card_side
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.spoof is not None:
            result['Spoof'] = self.spoof
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardSide') is not None:
            self.card_side = m.get('CardSide')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Spoof') is not None:
            self.spoof = m.get('Spoof')
        return self


class DocOcrResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_id_info: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        # Card and document recognition result	Only returned when the interface response is successful
        self.ext_id_info = ext_id_info
        # Whether the authentication passed.
        # 
        # - Y: Passed
        # - N: Not passed
        self.passed = passed
        # Sub-result code
        self.sub_code = sub_code
        # Unique identifier of the authentication request
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DocOcrResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DocOcrResponseBodyResult = None,
    ):
        # Return code
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Return result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DocOcrResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DocOcrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DocOcrResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DocOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DocOcrMaxRequest(TeaModel):
    def __init__(
        self,
        doc_page: str = None,
        doc_type: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_url: str = None,
        id_spoof: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        ocr_model: str = None,
        product_code: str = None,
        prompt: str = None,
        scene_code: str = None,
        spoof: str = None,
    ):
        self.doc_page = doc_page
        self.doc_type = doc_type
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        self.id_ocr_picture_url = id_ocr_picture_url
        self.id_spoof = id_spoof
        self.id_threshold = id_threshold
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.ocr_model = ocr_model
        self.product_code = product_code
        self.prompt = prompt
        self.scene_code = scene_code
        self.spoof = spoof

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_page is not None:
            result['DocPage'] = self.doc_page
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof
        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.ocr_model is not None:
            result['OcrModel'] = self.ocr_model
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.spoof is not None:
            result['Spoof'] = self.spoof
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocPage') is not None:
            self.doc_page = m.get('DocPage')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')
        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('OcrModel') is not None:
            self.ocr_model = m.get('OcrModel')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('Spoof') is not None:
            self.spoof = m.get('Spoof')
        return self


class DocOcrMaxResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_id_info: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        self.ext_id_info = ext_id_info
        self.passed = passed
        self.sub_code = sub_code
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DocOcrMaxResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: DocOcrMaxResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DocOcrMaxResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DocOcrMaxResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DocOcrMaxResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DocOcrMaxResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EkycVerifyRequest(TeaModel):
    def __init__(
        self,
        authorize: str = None,
        crop: str = None,
        doc_name: str = None,
        doc_no: str = None,
        doc_type: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_url: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
    ):
        self.authorize = authorize
        self.crop = crop
        self.doc_name = doc_name
        self.doc_no = doc_no
        self.doc_type = doc_type
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        self.id_ocr_picture_url = id_ocr_picture_url
        self.id_threshold = id_threshold
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize is not None:
            result['Authorize'] = self.authorize
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.doc_no is not None:
            result['DocNo'] = self.doc_no
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('DocNo') is not None:
            self.doc_no = m.get('DocNo')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class EkycVerifyResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_face_info: str = None,
        ext_id_info: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        self.ext_face_info = ext_face_info
        self.ext_id_info = ext_id_info
        self.passed = passed
        self.sub_code = sub_code
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtFaceInfo') is not None:
            self.ext_face_info = m.get('ExtFaceInfo')
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class EkycVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: EkycVerifyResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = EkycVerifyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EkycVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EkycVerifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = EkycVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceCompareRequest(TeaModel):
    def __init__(
        self,
        merchant_biz_id: str = None,
        source_face_picture: str = None,
        source_face_picture_url: str = None,
        target_face_picture: str = None,
        target_face_picture_url: str = None,
    ):
        self.merchant_biz_id = merchant_biz_id
        self.source_face_picture = source_face_picture
        self.source_face_picture_url = source_face_picture_url
        self.target_face_picture = target_face_picture
        self.target_face_picture_url = target_face_picture_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.source_face_picture is not None:
            result['SourceFacePicture'] = self.source_face_picture
        if self.source_face_picture_url is not None:
            result['SourceFacePictureUrl'] = self.source_face_picture_url
        if self.target_face_picture is not None:
            result['TargetFacePicture'] = self.target_face_picture
        if self.target_face_picture_url is not None:
            result['TargetFacePictureUrl'] = self.target_face_picture_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('SourceFacePicture') is not None:
            self.source_face_picture = m.get('SourceFacePicture')
        if m.get('SourceFacePictureUrl') is not None:
            self.source_face_picture_url = m.get('SourceFacePictureUrl')
        if m.get('TargetFacePicture') is not None:
            self.target_face_picture = m.get('TargetFacePicture')
        if m.get('TargetFacePictureUrl') is not None:
            self.target_face_picture_url = m.get('TargetFacePictureUrl')
        return self


class FaceCompareResponseBodyResult(TeaModel):
    def __init__(
        self,
        face_comparison_score: float = None,
        passed: str = None,
        transaction_id: str = None,
    ):
        self.face_comparison_score = face_comparison_score
        self.passed = passed
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class FaceCompareResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: FaceCompareResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = FaceCompareResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class FaceCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceCompareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FaceCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceGuardRiskRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        device_token: str = None,
        merchant_biz_id: str = None,
        product_code: str = None,
    ):
        self.biz_id = biz_id
        self.device_token = device_token
        self.merchant_biz_id = merchant_biz_id
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class FaceGuardRiskResponseBodyResult(TeaModel):
    def __init__(
        self,
        guard_risk_score: float = None,
        risk_extends: str = None,
        risk_tags: str = None,
        transaction_id: str = None,
    ):
        self.guard_risk_score = guard_risk_score
        self.risk_extends = risk_extends
        self.risk_tags = risk_tags
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guard_risk_score is not None:
            result['GuardRiskScore'] = self.guard_risk_score
        if self.risk_extends is not None:
            result['RiskExtends'] = self.risk_extends
        if self.risk_tags is not None:
            result['RiskTags'] = self.risk_tags
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuardRiskScore') is not None:
            self.guard_risk_score = m.get('GuardRiskScore')
        if m.get('RiskExtends') is not None:
            self.risk_extends = m.get('RiskExtends')
        if m.get('RiskTags') is not None:
            self.risk_tags = m.get('RiskTags')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class FaceGuardRiskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: FaceGuardRiskResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = FaceGuardRiskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class FaceGuardRiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceGuardRiskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FaceGuardRiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceLivenessRequest(TeaModel):
    def __init__(
        self,
        crop: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        face_quality: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        occlusion: str = None,
        product_code: str = None,
    ):
        self.crop = crop
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.face_quality = face_quality
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.occlusion = occlusion
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.occlusion is not None:
            result['Occlusion'] = self.occlusion
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('Occlusion') is not None:
            self.occlusion = m.get('Occlusion')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class FaceLivenessResponseBodyResultExtFaceInfo(TeaModel):
    def __init__(
        self,
        face_age: int = None,
        face_attack: str = None,
        face_gender: str = None,
        face_quality_score: float = None,
        occlusion_result: str = None,
    ):
        self.face_age = face_age
        self.face_attack = face_attack
        self.face_gender = face_gender
        self.face_quality_score = face_quality_score
        self.occlusion_result = occlusion_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_age is not None:
            result['FaceAge'] = self.face_age
        if self.face_attack is not None:
            result['FaceAttack'] = self.face_attack
        if self.face_gender is not None:
            result['FaceGender'] = self.face_gender
        if self.face_quality_score is not None:
            result['FaceQualityScore'] = self.face_quality_score
        if self.occlusion_result is not None:
            result['OcclusionResult'] = self.occlusion_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceAge') is not None:
            self.face_age = m.get('FaceAge')
        if m.get('FaceAttack') is not None:
            self.face_attack = m.get('FaceAttack')
        if m.get('FaceGender') is not None:
            self.face_gender = m.get('FaceGender')
        if m.get('FaceQualityScore') is not None:
            self.face_quality_score = m.get('FaceQualityScore')
        if m.get('OcclusionResult') is not None:
            self.occlusion_result = m.get('OcclusionResult')
        return self


class FaceLivenessResponseBodyResult(TeaModel):
    def __init__(
        self,
        ext_face_info: FaceLivenessResponseBodyResultExtFaceInfo = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        self.ext_face_info = ext_face_info
        self.passed = passed
        self.sub_code = sub_code
        self.transaction_id = transaction_id

    def validate(self):
        if self.ext_face_info:
            self.ext_face_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info.to_map()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtFaceInfo') is not None:
            temp_model = FaceLivenessResponseBodyResultExtFaceInfo()
            self.ext_face_info = temp_model.from_map(m['ExtFaceInfo'])
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class FaceLivenessResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: FaceLivenessResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = FaceLivenessResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class FaceLivenessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FaceLivenessResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FaceLivenessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FraudResultCallBackRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        ext_params: str = None,
        result_code: str = None,
        verify_deploy_env: str = None,
    ):
        self.certify_id = certify_id
        self.ext_params = ext_params
        self.result_code = result_code
        self.verify_deploy_env = verify_deploy_env

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.verify_deploy_env is not None:
            result['VerifyDeployEnv'] = self.verify_deploy_env
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('VerifyDeployEnv') is not None:
            self.verify_deploy_env = m.get('VerifyDeployEnv')
        return self


class FraudResultCallBackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FraudResultCallBackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FraudResultCallBackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FraudResultCallBackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id2MetaPeriodVerifyIntlRequest(TeaModel):
    def __init__(
        self,
        doc_name: str = None,
        doc_no: str = None,
        doc_type: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
        scene_code: str = None,
        validity_end_date: str = None,
        validity_start_date: str = None,
    ):
        # This parameter is required.
        self.doc_name = doc_name
        # This parameter is required.
        self.doc_no = doc_no
        # This parameter is required.
        self.doc_type = doc_type
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        # This parameter is required.
        self.product_code = product_code
        self.scene_code = scene_code
        # This parameter is required.
        self.validity_end_date = validity_end_date
        # This parameter is required.
        self.validity_start_date = validity_start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.doc_no is not None:
            result['DocNo'] = self.doc_no
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.validity_end_date is not None:
            result['ValidityEndDate'] = self.validity_end_date
        if self.validity_start_date is not None:
            result['ValidityStartDate'] = self.validity_start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('DocNo') is not None:
            self.doc_no = m.get('DocNo')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ValidityEndDate') is not None:
            self.validity_end_date = m.get('ValidityEndDate')
        if m.get('ValidityStartDate') is not None:
            self.validity_start_date = m.get('ValidityStartDate')
        return self


class Id2MetaPeriodVerifyIntlResponseBodyResult(TeaModel):
    def __init__(
        self,
        passed: str = None,
        sub_code: str = None,
    ):
        self.passed = passed
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class Id2MetaPeriodVerifyIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Id2MetaPeriodVerifyIntlResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = Id2MetaPeriodVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class Id2MetaPeriodVerifyIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Id2MetaPeriodVerifyIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Id2MetaPeriodVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id2MetaVerifyIntlRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        product_code: str = None,
        user_name: str = None,
    ):
        self.identify_num = identify_num
        self.param_type = param_type
        self.product_code = product_code
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Id2MetaVerifyIntlResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
    ):
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        return self


class Id2MetaVerifyIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Id2MetaVerifyIntlResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = Id2MetaVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class Id2MetaVerifyIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Id2MetaVerifyIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Id2MetaVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeRequest(TeaModel):
    def __init__(
        self,
        app_quality_check: str = None,
        authorize: str = None,
        callback_token: str = None,
        callback_url: str = None,
        chameleon_frame_enable: str = None,
        crop: str = None,
        date_of_birth: str = None,
        date_of_expiry: str = None,
        doc_name: str = None,
        doc_no: str = None,
        doc_page_config: List[str] = None,
        doc_scan_mode: str = None,
        doc_type: str = None,
        doc_video: str = None,
        document_number: str = None,
        edit_ocr_result: str = None,
        experience_code: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        id_face_quality: str = None,
        id_spoof: str = None,
        id_threshold: str = None,
        language_config: str = None,
        mrtdinput: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        meta_info: str = None,
        model: str = None,
        ocr: str = None,
        pages: str = None,
        procedure_priority: str = None,
        product_code: str = None,
        product_flow: str = None,
        return_url: str = None,
        scene_code: str = None,
        security_level: str = None,
        show_album_icon: str = None,
        show_guide_page: str = None,
        show_ocr_result: str = None,
        style_config: str = None,
        use_nfc: str = None,
    ):
        self.app_quality_check = app_quality_check
        self.authorize = authorize
        self.callback_token = callback_token
        self.callback_url = callback_url
        self.chameleon_frame_enable = chameleon_frame_enable
        self.crop = crop
        self.date_of_birth = date_of_birth
        self.date_of_expiry = date_of_expiry
        self.doc_name = doc_name
        self.doc_no = doc_no
        self.doc_page_config = doc_page_config
        self.doc_scan_mode = doc_scan_mode
        self.doc_type = doc_type
        self.doc_video = doc_video
        self.document_number = document_number
        self.edit_ocr_result = edit_ocr_result
        self.experience_code = experience_code
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.id_face_quality = id_face_quality
        self.id_spoof = id_spoof
        self.id_threshold = id_threshold
        self.language_config = language_config
        self.mrtdinput = mrtdinput
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.meta_info = meta_info
        self.model = model
        # OCR。
        self.ocr = ocr
        self.pages = pages
        self.procedure_priority = procedure_priority
        self.product_code = product_code
        self.product_flow = product_flow
        self.return_url = return_url
        self.scene_code = scene_code
        self.security_level = security_level
        self.show_album_icon = show_album_icon
        self.show_guide_page = show_guide_page
        self.show_ocr_result = show_ocr_result
        self.style_config = style_config
        self.use_nfc = use_nfc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_quality_check is not None:
            result['AppQualityCheck'] = self.app_quality_check
        if self.authorize is not None:
            result['Authorize'] = self.authorize
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.chameleon_frame_enable is not None:
            result['ChameleonFrameEnable'] = self.chameleon_frame_enable
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.date_of_birth is not None:
            result['DateOfBirth'] = self.date_of_birth
        if self.date_of_expiry is not None:
            result['DateOfExpiry'] = self.date_of_expiry
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.doc_no is not None:
            result['DocNo'] = self.doc_no
        if self.doc_page_config is not None:
            result['DocPageConfig'] = self.doc_page_config
        if self.doc_scan_mode is not None:
            result['DocScanMode'] = self.doc_scan_mode
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.doc_video is not None:
            result['DocVideo'] = self.doc_video
        if self.document_number is not None:
            result['DocumentNumber'] = self.document_number
        if self.edit_ocr_result is not None:
            result['EditOcrResult'] = self.edit_ocr_result
        if self.experience_code is not None:
            result['ExperienceCode'] = self.experience_code
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof
        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold
        if self.language_config is not None:
            result['LanguageConfig'] = self.language_config
        if self.mrtdinput is not None:
            result['MRTDInput'] = self.mrtdinput
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.model is not None:
            result['Model'] = self.model
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.procedure_priority is not None:
            result['ProcedurePriority'] = self.procedure_priority
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_flow is not None:
            result['ProductFlow'] = self.product_flow
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.show_album_icon is not None:
            result['ShowAlbumIcon'] = self.show_album_icon
        if self.show_guide_page is not None:
            result['ShowGuidePage'] = self.show_guide_page
        if self.show_ocr_result is not None:
            result['ShowOcrResult'] = self.show_ocr_result
        if self.style_config is not None:
            result['StyleConfig'] = self.style_config
        if self.use_nfc is not None:
            result['UseNFC'] = self.use_nfc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppQualityCheck') is not None:
            self.app_quality_check = m.get('AppQualityCheck')
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ChameleonFrameEnable') is not None:
            self.chameleon_frame_enable = m.get('ChameleonFrameEnable')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DateOfBirth') is not None:
            self.date_of_birth = m.get('DateOfBirth')
        if m.get('DateOfExpiry') is not None:
            self.date_of_expiry = m.get('DateOfExpiry')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('DocNo') is not None:
            self.doc_no = m.get('DocNo')
        if m.get('DocPageConfig') is not None:
            self.doc_page_config = m.get('DocPageConfig')
        if m.get('DocScanMode') is not None:
            self.doc_scan_mode = m.get('DocScanMode')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('DocVideo') is not None:
            self.doc_video = m.get('DocVideo')
        if m.get('DocumentNumber') is not None:
            self.document_number = m.get('DocumentNumber')
        if m.get('EditOcrResult') is not None:
            self.edit_ocr_result = m.get('EditOcrResult')
        if m.get('ExperienceCode') is not None:
            self.experience_code = m.get('ExperienceCode')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')
        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')
        if m.get('LanguageConfig') is not None:
            self.language_config = m.get('LanguageConfig')
        if m.get('MRTDInput') is not None:
            self.mrtdinput = m.get('MRTDInput')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('ProcedurePriority') is not None:
            self.procedure_priority = m.get('ProcedurePriority')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductFlow') is not None:
            self.product_flow = m.get('ProductFlow')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('ShowAlbumIcon') is not None:
            self.show_album_icon = m.get('ShowAlbumIcon')
        if m.get('ShowGuidePage') is not None:
            self.show_guide_page = m.get('ShowGuidePage')
        if m.get('ShowOcrResult') is not None:
            self.show_ocr_result = m.get('ShowOcrResult')
        if m.get('StyleConfig') is not None:
            self.style_config = m.get('StyleConfig')
        if m.get('UseNFC') is not None:
            self.use_nfc = m.get('UseNFC')
        return self


class InitializeShrinkRequest(TeaModel):
    def __init__(
        self,
        app_quality_check: str = None,
        authorize: str = None,
        callback_token: str = None,
        callback_url: str = None,
        chameleon_frame_enable: str = None,
        crop: str = None,
        date_of_birth: str = None,
        date_of_expiry: str = None,
        doc_name: str = None,
        doc_no: str = None,
        doc_page_config_shrink: str = None,
        doc_scan_mode: str = None,
        doc_type: str = None,
        doc_video: str = None,
        document_number: str = None,
        edit_ocr_result: str = None,
        experience_code: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        id_face_quality: str = None,
        id_spoof: str = None,
        id_threshold: str = None,
        language_config: str = None,
        mrtdinput: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        meta_info: str = None,
        model: str = None,
        ocr: str = None,
        pages: str = None,
        procedure_priority: str = None,
        product_code: str = None,
        product_flow: str = None,
        return_url: str = None,
        scene_code: str = None,
        security_level: str = None,
        show_album_icon: str = None,
        show_guide_page: str = None,
        show_ocr_result: str = None,
        style_config: str = None,
        use_nfc: str = None,
    ):
        self.app_quality_check = app_quality_check
        self.authorize = authorize
        self.callback_token = callback_token
        self.callback_url = callback_url
        self.chameleon_frame_enable = chameleon_frame_enable
        self.crop = crop
        self.date_of_birth = date_of_birth
        self.date_of_expiry = date_of_expiry
        self.doc_name = doc_name
        self.doc_no = doc_no
        self.doc_page_config_shrink = doc_page_config_shrink
        self.doc_scan_mode = doc_scan_mode
        self.doc_type = doc_type
        self.doc_video = doc_video
        self.document_number = document_number
        self.edit_ocr_result = edit_ocr_result
        self.experience_code = experience_code
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.id_face_quality = id_face_quality
        self.id_spoof = id_spoof
        self.id_threshold = id_threshold
        self.language_config = language_config
        self.mrtdinput = mrtdinput
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.meta_info = meta_info
        self.model = model
        # OCR。
        self.ocr = ocr
        self.pages = pages
        self.procedure_priority = procedure_priority
        self.product_code = product_code
        self.product_flow = product_flow
        self.return_url = return_url
        self.scene_code = scene_code
        self.security_level = security_level
        self.show_album_icon = show_album_icon
        self.show_guide_page = show_guide_page
        self.show_ocr_result = show_ocr_result
        self.style_config = style_config
        self.use_nfc = use_nfc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_quality_check is not None:
            result['AppQualityCheck'] = self.app_quality_check
        if self.authorize is not None:
            result['Authorize'] = self.authorize
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.chameleon_frame_enable is not None:
            result['ChameleonFrameEnable'] = self.chameleon_frame_enable
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.date_of_birth is not None:
            result['DateOfBirth'] = self.date_of_birth
        if self.date_of_expiry is not None:
            result['DateOfExpiry'] = self.date_of_expiry
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.doc_no is not None:
            result['DocNo'] = self.doc_no
        if self.doc_page_config_shrink is not None:
            result['DocPageConfig'] = self.doc_page_config_shrink
        if self.doc_scan_mode is not None:
            result['DocScanMode'] = self.doc_scan_mode
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.doc_video is not None:
            result['DocVideo'] = self.doc_video
        if self.document_number is not None:
            result['DocumentNumber'] = self.document_number
        if self.edit_ocr_result is not None:
            result['EditOcrResult'] = self.edit_ocr_result
        if self.experience_code is not None:
            result['ExperienceCode'] = self.experience_code
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof
        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold
        if self.language_config is not None:
            result['LanguageConfig'] = self.language_config
        if self.mrtdinput is not None:
            result['MRTDInput'] = self.mrtdinput
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.model is not None:
            result['Model'] = self.model
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.procedure_priority is not None:
            result['ProcedurePriority'] = self.procedure_priority
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_flow is not None:
            result['ProductFlow'] = self.product_flow
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.show_album_icon is not None:
            result['ShowAlbumIcon'] = self.show_album_icon
        if self.show_guide_page is not None:
            result['ShowGuidePage'] = self.show_guide_page
        if self.show_ocr_result is not None:
            result['ShowOcrResult'] = self.show_ocr_result
        if self.style_config is not None:
            result['StyleConfig'] = self.style_config
        if self.use_nfc is not None:
            result['UseNFC'] = self.use_nfc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppQualityCheck') is not None:
            self.app_quality_check = m.get('AppQualityCheck')
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ChameleonFrameEnable') is not None:
            self.chameleon_frame_enable = m.get('ChameleonFrameEnable')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DateOfBirth') is not None:
            self.date_of_birth = m.get('DateOfBirth')
        if m.get('DateOfExpiry') is not None:
            self.date_of_expiry = m.get('DateOfExpiry')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('DocNo') is not None:
            self.doc_no = m.get('DocNo')
        if m.get('DocPageConfig') is not None:
            self.doc_page_config_shrink = m.get('DocPageConfig')
        if m.get('DocScanMode') is not None:
            self.doc_scan_mode = m.get('DocScanMode')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('DocVideo') is not None:
            self.doc_video = m.get('DocVideo')
        if m.get('DocumentNumber') is not None:
            self.document_number = m.get('DocumentNumber')
        if m.get('EditOcrResult') is not None:
            self.edit_ocr_result = m.get('EditOcrResult')
        if m.get('ExperienceCode') is not None:
            self.experience_code = m.get('ExperienceCode')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')
        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')
        if m.get('LanguageConfig') is not None:
            self.language_config = m.get('LanguageConfig')
        if m.get('MRTDInput') is not None:
            self.mrtdinput = m.get('MRTDInput')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('ProcedurePriority') is not None:
            self.procedure_priority = m.get('ProcedurePriority')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductFlow') is not None:
            self.product_flow = m.get('ProductFlow')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('ShowAlbumIcon') is not None:
            self.show_album_icon = m.get('ShowAlbumIcon')
        if m.get('ShowGuidePage') is not None:
            self.show_guide_page = m.get('ShowGuidePage')
        if m.get('ShowOcrResult') is not None:
            self.show_ocr_result = m.get('ShowOcrResult')
        if m.get('StyleConfig') is not None:
            self.style_config = m.get('StyleConfig')
        if m.get('UseNFC') is not None:
            self.use_nfc = m.get('UseNFC')
        return self


class InitializeResponseBodyResult(TeaModel):
    def __init__(
        self,
        client_cfg: str = None,
        protocol: str = None,
        transaction_id: str = None,
        transaction_url: str = None,
    ):
        self.client_cfg = client_cfg
        self.protocol = protocol
        self.transaction_id = transaction_id
        self.transaction_url = transaction_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_cfg is not None:
            result['ClientCfg'] = self.client_cfg
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        if self.transaction_url is not None:
            result['TransactionUrl'] = self.transaction_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientCfg') is not None:
            self.client_cfg = m.get('ClientCfg')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        if m.get('TransactionUrl') is not None:
            self.transaction_url = m.get('TransactionUrl')
        return self


class InitializeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: InitializeResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = InitializeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class InitializeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitializeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = InitializeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KeepaliveIntlResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: str = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class KeepaliveIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: KeepaliveIntlResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = KeepaliveIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class KeepaliveIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KeepaliveIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = KeepaliveIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile2MetaVerifyIntlRequest(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        param_type: str = None,
        product_code: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.mobile = mobile
        # This parameter is required.
        self.param_type = param_type
        # This parameter is required.
        self.product_code = product_code
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile2MetaVerifyIntlResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
    ):
        self.biz_code = biz_code
        self.isp_name = isp_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        return self


class Mobile2MetaVerifyIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Mobile2MetaVerifyIntlResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = Mobile2MetaVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class Mobile2MetaVerifyIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Mobile2MetaVerifyIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Mobile2MetaVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile3MetaVerifyIntlRequest(TeaModel):
    def __init__(
        self,
        identify_num: str = None,
        mobile: str = None,
        param_type: str = None,
        product_code: str = None,
        user_name: str = None,
    ):
        # ID number
        # 
        # - When paramType is set to normal, enter the plaintext
        # - When paramType is set to md5, enter a 32-character lowercase md5 string
        self.identify_num = identify_num
        # Mobile phone number.
        # 
        # - When paramType is set to normal, enter the plaintext
        # - When paramType is set to md5, enter a 32-character lowercase md5 string
        self.mobile = mobile
        # Parameter type:
        # 
        # - normal: unencrypted
        # - md5: md5 encrypted
        self.param_type = param_type
        # The product solution to be integrated, with a fixed value: MOBILE_3META
        self.product_code = product_code
        # Name
        # 
        # - When paramType is set to normal, enter the plaintext
        # - When paramType is set to md5, enter a 32-character lowercase md5 string
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile3MetaVerifyIntlResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
        sub_code: str = None,
    ):
        # Verification result code.
        # - 1: Verification consistent
        # - 2: Verification inconsistent
        # - 3: No record found
        self.biz_code = biz_code
        # ISP name
        # 
        # - CMCC: China Mobile
        # - CUCC: China Unicom
        # - CTCC: China Telecom
        self.isp_name = isp_name
        # Detailed verification results
        # 
        # - 101: Verification passed 
        # - 201: Mobile number and name do not match, mobile number and ID number do not match 
        # - 202: Mobile number and name match, but mobile number and ID number do not match 
        # - 203: Mobile number and ID number match, but mobile number and name do not match 
        # - 204: Other inconsistencies
        # - 301: No record found
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class Mobile3MetaVerifyIntlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Mobile3MetaVerifyIntlResponseBodyResult = None,
    ):
        # Return code
        self.code = code
        # Return message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Return result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = Mobile3MetaVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class Mobile3MetaVerifyIntlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Mobile3MetaVerifyIntlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = Mobile3MetaVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


