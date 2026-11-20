# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePickUpWaybillShrinkRequest(DaraModel):
    def __init__(
        self,
        appoint_got_end_time: str = None,
        appoint_got_start_time: str = None,
        biz_type: int = None,
        consignee_address_shrink: str = None,
        consignee_mobile: str = None,
        consignee_name: str = None,
        consignee_phone: str = None,
        cp_code: str = None,
        goods_infos_shrink: str = None,
        order_channels: str = None,
        outer_order_code: str = None,
        remark: str = None,
        send_address_shrink: str = None,
        send_mobile: str = None,
        send_name: str = None,
        send_phone: str = None,
    ):
        # The end time of the scheduled door-to-door pickup, in the YYYY-MM-DD HH:mm:ss format. To obtain the value of **AppointGotEndTime**, obtain the **EndTime** value from **AppointTimes** in the **CpTimeSelectList** response parameter of the [CreatePickUpWaybillPreQuery](https://api.aliyun.com/document/Dyplsapi/2017-05-25/CreatePickUpWaybillPreQuery) operation.
        # > Required when **bizType** is set to **1**.
        self.appoint_got_end_time = appoint_got_end_time
        # The start time of the scheduled door-to-door pickup, in the YYYY-MM-DD HH:mm:ss format. To obtain the value of **AppointGotStartTime**, obtain the **StartTime** value from **AppointTimes** in the **CpTimeSelectList** response parameter of the [CreatePickUpWaybillPreQuery](https://api.aliyun.com/document/Dyplsapi/2017-05-25/CreatePickUpWaybillPreQuery) operation.
        # 
        # > Required when **bizType** is set to **1**.
        self.appoint_got_start_time = appoint_got_start_time
        # The delivery mode. Valid values:
        # 
        # - **0**: real-time order (default)
        # - **1**: scheduled order
        self.biz_type = biz_type
        # The address of the recipient.
        # 
        # This parameter is required.
        self.consignee_address_shrink = consignee_address_shrink
        # The mobile phone number of the recipient.
        # 
        # > You must specify either ConsigneeMobile or ConsigneePhone.
        self.consignee_mobile = consignee_mobile
        # The name of the recipient.
        # 
        # This parameter is required.
        self.consignee_name = consignee_name
        # The landline phone number of the recipient.
        # > You must specify either ConsigneeMobile or ConsigneePhone.
        self.consignee_phone = consignee_phone
        # The express delivery company code.
        self.cp_code = cp_code
        # The list of goods.
        self.goods_infos_shrink = goods_infos_shrink
        # The external channel source.
        # 
        # This parameter is required.
        self.order_channels = order_channels
        # The external order ID.
        # 
        # This parameter is required.
        self.outer_order_code = outer_order_code
        # The remark. The remark content printed on the waybill.
        self.remark = remark
        # The address of the sender.
        # 
        # This parameter is required.
        self.send_address_shrink = send_address_shrink
        # The mobile phone number of the sender.
        # 
        # > You must specify either SendMobile or SendPhone.
        self.send_mobile = send_mobile
        # The name of the sender.
        # 
        # This parameter is required.
        self.send_name = send_name
        # The landline phone number of the sender.
        # > You must specify either SendMobile or SendPhone.
        self.send_phone = send_phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appoint_got_end_time is not None:
            result['AppointGotEndTime'] = self.appoint_got_end_time

        if self.appoint_got_start_time is not None:
            result['AppointGotStartTime'] = self.appoint_got_start_time

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.consignee_address_shrink is not None:
            result['ConsigneeAddress'] = self.consignee_address_shrink

        if self.consignee_mobile is not None:
            result['ConsigneeMobile'] = self.consignee_mobile

        if self.consignee_name is not None:
            result['ConsigneeName'] = self.consignee_name

        if self.consignee_phone is not None:
            result['ConsigneePhone'] = self.consignee_phone

        if self.cp_code is not None:
            result['CpCode'] = self.cp_code

        if self.goods_infos_shrink is not None:
            result['GoodsInfos'] = self.goods_infos_shrink

        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels

        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.send_address_shrink is not None:
            result['SendAddress'] = self.send_address_shrink

        if self.send_mobile is not None:
            result['SendMobile'] = self.send_mobile

        if self.send_name is not None:
            result['SendName'] = self.send_name

        if self.send_phone is not None:
            result['SendPhone'] = self.send_phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppointGotEndTime') is not None:
            self.appoint_got_end_time = m.get('AppointGotEndTime')

        if m.get('AppointGotStartTime') is not None:
            self.appoint_got_start_time = m.get('AppointGotStartTime')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ConsigneeAddress') is not None:
            self.consignee_address_shrink = m.get('ConsigneeAddress')

        if m.get('ConsigneeMobile') is not None:
            self.consignee_mobile = m.get('ConsigneeMobile')

        if m.get('ConsigneeName') is not None:
            self.consignee_name = m.get('ConsigneeName')

        if m.get('ConsigneePhone') is not None:
            self.consignee_phone = m.get('ConsigneePhone')

        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')

        if m.get('GoodsInfos') is not None:
            self.goods_infos_shrink = m.get('GoodsInfos')

        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')

        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SendAddress') is not None:
            self.send_address_shrink = m.get('SendAddress')

        if m.get('SendMobile') is not None:
            self.send_mobile = m.get('SendMobile')

        if m.get('SendName') is not None:
            self.send_name = m.get('SendName')

        if m.get('SendPhone') is not None:
            self.send_phone = m.get('SendPhone')

        return self

