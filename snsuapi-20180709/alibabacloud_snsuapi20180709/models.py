# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class BandOfferOrderRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        band_id: str = None,
        offer_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.band_id = band_id
        self.offer_id = offer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.band_id is not None:
            result['BandId'] = self.band_id
        if self.offer_id is not None:
            result['OfferId'] = self.offer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('BandId') is not None:
            self.band_id = m.get('BandId')
        if m.get('OfferId') is not None:
            self.offer_id = m.get('OfferId')
        return self


class BandOfferOrderResponseBodyResultModule(TeaModel):
    def __init__(
        self,
        lx_order_id: int = None,
    ):
        self.lx_order_id = lx_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lx_order_id is not None:
            result['LxOrderId'] = self.lx_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LxOrderId') is not None:
            self.lx_order_id = m.get('LxOrderId')
        return self


class BandOfferOrderResponseBody(TeaModel):
    def __init__(
        self,
        result_module: BandOfferOrderResponseBodyResultModule = None,
        request_id: str = None,
        result_message: str = None,
        result_code: str = None,
    ):
        self.result_module = result_module
        self.request_id = request_id
        self.result_message = result_message
        self.result_code = result_code

    def validate(self):
        if self.result_module:
            self.result_module.validate()

    def to_map(self):
        result = dict()
        if self.result_module is not None:
            result['ResultModule'] = self.result_module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultModule') is not None:
            temp_model = BandOfferOrderResponseBodyResultModule()
            self.result_module = temp_model.from_map(m['ResultModule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class BandOfferOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BandOfferOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BandOfferOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandPrecheckRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ip_address: str = None,
        port: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.ip_address = ip_address
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class BandPrecheckResponseBodyResultModuleBandOfferListBandOfferList(TeaModel):
    def __init__(
        self,
        direction: str = None,
        offer_id: int = None,
        bandwidth: int = None,
        duration: int = None,
    ):
        self.direction = direction
        self.offer_id = offer_id
        self.bandwidth = bandwidth
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.offer_id is not None:
            result['OfferId'] = self.offer_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('OfferId') is not None:
            self.offer_id = m.get('OfferId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class BandPrecheckResponseBodyResultModuleBandOfferList(TeaModel):
    def __init__(
        self,
        band_offer_list: List[BandPrecheckResponseBodyResultModuleBandOfferListBandOfferList] = None,
    ):
        self.band_offer_list = band_offer_list

    def validate(self):
        if self.band_offer_list:
            for k in self.band_offer_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BandOfferList'] = []
        if self.band_offer_list is not None:
            for k in self.band_offer_list:
                result['BandOfferList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_offer_list = []
        if m.get('BandOfferList') is not None:
            for k in m.get('BandOfferList'):
                temp_model = BandPrecheckResponseBodyResultModuleBandOfferListBandOfferList()
                self.band_offer_list.append(temp_model.from_map(k))
        return self


class BandPrecheckResponseBodyResultModule(TeaModel):
    def __init__(
        self,
        upload_bandwidth: int = None,
        band_id: int = None,
        band_offer_list: BandPrecheckResponseBodyResultModuleBandOfferList = None,
        download_bandwidth: int = None,
    ):
        self.upload_bandwidth = upload_bandwidth
        self.band_id = band_id
        self.band_offer_list = band_offer_list
        self.download_bandwidth = download_bandwidth

    def validate(self):
        if self.band_offer_list:
            self.band_offer_list.validate()

    def to_map(self):
        result = dict()
        if self.upload_bandwidth is not None:
            result['UploadBandwidth'] = self.upload_bandwidth
        if self.band_id is not None:
            result['BandId'] = self.band_id
        if self.band_offer_list is not None:
            result['BandOfferList'] = self.band_offer_list.to_map()
        if self.download_bandwidth is not None:
            result['DownloadBandwidth'] = self.download_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UploadBandwidth') is not None:
            self.upload_bandwidth = m.get('UploadBandwidth')
        if m.get('BandId') is not None:
            self.band_id = m.get('BandId')
        if m.get('BandOfferList') is not None:
            temp_model = BandPrecheckResponseBodyResultModuleBandOfferList()
            self.band_offer_list = temp_model.from_map(m['BandOfferList'])
        if m.get('DownloadBandwidth') is not None:
            self.download_bandwidth = m.get('DownloadBandwidth')
        return self


class BandPrecheckResponseBody(TeaModel):
    def __init__(
        self,
        result_module: BandPrecheckResponseBodyResultModule = None,
        request_id: str = None,
        result_message: str = None,
        result_code: str = None,
    ):
        self.result_module = result_module
        self.request_id = request_id
        self.result_message = result_message
        self.result_code = result_code

    def validate(self):
        if self.result_module:
            self.result_module.validate()

    def to_map(self):
        result = dict()
        if self.result_module is not None:
            result['ResultModule'] = self.result_module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultModule') is not None:
            temp_model = BandPrecheckResponseBodyResultModule()
            self.result_module = temp_model.from_map(m['ResultModule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class BandPrecheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BandPrecheckResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BandPrecheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandStartSpeedUpRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ip_address: str = None,
        port: int = None,
        band_id: int = None,
        direction: str = None,
        target_bandwidth: int = None,
        band_scene: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.ip_address = ip_address
        self.port = port
        self.band_id = band_id
        self.direction = direction
        self.target_bandwidth = target_bandwidth
        self.band_scene = band_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.port is not None:
            result['Port'] = self.port
        if self.band_id is not None:
            result['BandId'] = self.band_id
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.target_bandwidth is not None:
            result['TargetBandwidth'] = self.target_bandwidth
        if self.band_scene is not None:
            result['BandScene'] = self.band_scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('BandId') is not None:
            self.band_id = m.get('BandId')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('TargetBandwidth') is not None:
            self.target_bandwidth = m.get('TargetBandwidth')
        if m.get('BandScene') is not None:
            self.band_scene = m.get('BandScene')
        return self


class BandStartSpeedUpResponseBody(TeaModel):
    def __init__(
        self,
        result_module: bool = None,
        request_id: str = None,
        result_message: str = None,
        result_code: str = None,
    ):
        self.result_module = result_module
        self.request_id = request_id
        self.result_message = result_message
        self.result_code = result_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result_module is not None:
            result['ResultModule'] = self.result_module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultModule') is not None:
            self.result_module = m.get('ResultModule')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class BandStartSpeedUpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BandStartSpeedUpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BandStartSpeedUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandStatusQueryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        band_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.band_id = band_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.band_id is not None:
            result['BandId'] = self.band_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('BandId') is not None:
            self.band_id = m.get('BandId')
        return self


class BandStatusQueryResponseBodyResultModule(TeaModel):
    def __init__(
        self,
        upload_target: int = None,
        download_target: int = None,
    ):
        self.upload_target = upload_target
        self.download_target = download_target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.upload_target is not None:
            result['UploadTarget'] = self.upload_target
        if self.download_target is not None:
            result['DownloadTarget'] = self.download_target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UploadTarget') is not None:
            self.upload_target = m.get('UploadTarget')
        if m.get('DownloadTarget') is not None:
            self.download_target = m.get('DownloadTarget')
        return self


class BandStatusQueryResponseBody(TeaModel):
    def __init__(
        self,
        result_module: BandStatusQueryResponseBodyResultModule = None,
        request_id: str = None,
        result_message: str = None,
        result_code: str = None,
    ):
        self.result_module = result_module
        self.request_id = request_id
        self.result_message = result_message
        self.result_code = result_code

    def validate(self):
        if self.result_module:
            self.result_module.validate()

    def to_map(self):
        result = dict()
        if self.result_module is not None:
            result['ResultModule'] = self.result_module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultModule') is not None:
            temp_model = BandStatusQueryResponseBodyResultModule()
            self.result_module = temp_model.from_map(m['ResultModule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class BandStatusQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BandStatusQueryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BandStatusQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandStopSpeedUpRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ip_address: str = None,
        port: int = None,
        band_id: int = None,
        direction: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.ip_address = ip_address
        self.port = port
        self.band_id = band_id
        self.direction = direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.port is not None:
            result['Port'] = self.port
        if self.band_id is not None:
            result['BandId'] = self.band_id
        if self.direction is not None:
            result['Direction'] = self.direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('BandId') is not None:
            self.band_id = m.get('BandId')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        return self


class BandStopSpeedUpResponseBody(TeaModel):
    def __init__(
        self,
        result_module: bool = None,
        request_id: str = None,
        result_message: str = None,
        result_code: str = None,
    ):
        self.result_module = result_module
        self.request_id = request_id
        self.result_message = result_message
        self.result_code = result_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result_module is not None:
            result['ResultModule'] = self.result_module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultModule') is not None:
            self.result_module = m.get('ResultModule')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class BandStopSpeedUpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BandStopSpeedUpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BandStopSpeedUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MobileStartSpeedUpRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        token: str = None,
        duration: str = None,
        ip: str = None,
        public_ip: str = None,
        public_port: str = None,
        destination_ip_address: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.token = token
        self.duration = duration
        self.ip = ip
        self.public_ip = public_ip
        self.public_port = public_port
        self.destination_ip_address = destination_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.token is not None:
            result['Token'] = self.token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.public_port is not None:
            result['PublicPort'] = self.public_port
        if self.destination_ip_address is not None:
            result['DestinationIpAddress'] = self.destination_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('PublicPort') is not None:
            self.public_port = m.get('PublicPort')
        if m.get('DestinationIpAddress') is not None:
            self.destination_ip_address = m.get('DestinationIpAddress')
        return self


class MobileStartSpeedUpResponseBody(TeaModel):
    def __init__(
        self,
        result_module: str = None,
        request_id: str = None,
        result_message: str = None,
        result_code: str = None,
    ):
        self.result_module = result_module
        self.request_id = request_id
        self.result_message = result_message
        self.result_code = result_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result_module is not None:
            result['ResultModule'] = self.result_module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultModule') is not None:
            self.result_module = m.get('ResultModule')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class MobileStartSpeedUpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MobileStartSpeedUpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MobileStartSpeedUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MobileStatusQueryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        correlation_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.correlation_id = correlation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.correlation_id is not None:
            result['CorrelationId'] = self.correlation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CorrelationId') is not None:
            self.correlation_id = m.get('CorrelationId')
        return self


class MobileStatusQueryResponseBody(TeaModel):
    def __init__(
        self,
        result_module: bool = None,
        request_id: str = None,
        result_message: str = None,
        result_code: str = None,
    ):
        self.result_module = result_module
        self.request_id = request_id
        self.result_message = result_message
        self.result_code = result_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result_module is not None:
            result['ResultModule'] = self.result_module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultModule') is not None:
            self.result_module = m.get('ResultModule')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class MobileStatusQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MobileStatusQueryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MobileStatusQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MobileStopSpeedUpRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        correlation_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.correlation_id = correlation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.correlation_id is not None:
            result['CorrelationId'] = self.correlation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CorrelationId') is not None:
            self.correlation_id = m.get('CorrelationId')
        return self


class MobileStopSpeedUpResponseBody(TeaModel):
    def __init__(
        self,
        result_module: bool = None,
        request_id: str = None,
        result_message: str = None,
        result_code: str = None,
    ):
        self.result_module = result_module
        self.request_id = request_id
        self.result_message = result_message
        self.result_code = result_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result_module is not None:
            result['ResultModule'] = self.result_module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultModule') is not None:
            self.result_module = m.get('ResultModule')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        return self


class MobileStopSpeedUpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MobileStopSpeedUpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MobileStopSpeedUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


