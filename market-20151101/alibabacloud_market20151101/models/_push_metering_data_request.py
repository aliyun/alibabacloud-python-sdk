# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushMeteringDataRequest(DaraModel):
    def __init__(
        self,
        metering: str = None,
    ):
        # The metric description in the example is as follows:
        # 
        # - InstanceId: instance ID of the Alibaba Cloud Marketplace instance. The parameter type is String.
        # - StartTime: the start time of the metering period. Unit: seconds. The value is a UNIX timestamp, such as 1723771200. The parameter type is Long.
        # - EndTime: the end time of the metering period. Unit: seconds. The value is a UNIX timestamp, such as 1723771800. The parameter type is Long.
        # - Entities: the metering entity objects. The parameter type is List<Map>.
        #     - Key: the name of the metering item property. The parameter type is String.
        #         - Frequency: the number of uses (times).
        #         - Period: the usage duration in hours (seconds).
        #          Note: The unit of duration in the request parameter is seconds, while the billing unit is hours. Therefore, the duration is transformed to hours during billing. For example, if the pushed usage for 19:00 to 20:00 is 1800 and the billing price is 1 CNY/hour, the fee for this period billed hourly is 1800 / 3600 x 1 = 0.5 CNY. If the fee is a decimal, two decimal places are retained, and the excess is discarded.
        # 
        #         - Storage: the used storage space (bytes).
        # 
        #          Note: The unit in the request parameter is bytes, while the billing unit is MB. Therefore, the value is transformed to MB during billing. For example, if the pushed usage for 19:00 to 20:00 is 524288 and the billing price is 1 CNY/MB, the fee for this period billed hourly is 524288 / 1024 / 1024 x 1 = 0.5 CNY. If the fee is a decimal, two decimal places are retained, and the excess is discarded.
        # 
        #         - NetworkOut: the outbound traffic used (bits).
        # 
        #          Note: The unit in the request parameter is bits, while the billing unit is Mbit. Therefore, the value is transformed to Mbit during billing. For example, if the pushed usage for 19:00 to 20:00 is 524288 and the billing price is 1 CNY/Mbit, the fee for this period billed hourly is 524288 / 1024 / 1024 x 1 = 0.5 CNY. If the fee is a decimal, two decimal places are retained, and the excess is discarded.
        # 
        #         - NetworkIn: the inbound traffic used (bits).
        # 
        #          Note: The unit in the request parameter is bits, while the billing unit is Mbit. Therefore, the value is transformed to Mbit during billing. For example, if the pushed usage for 19:00 to 20:00 is 524288 and the billing price is 1 CNY/Mbit, the fee for this period billed hourly is 524288 / 1024 / 1024 x 1 = 0.5 CNY. If the fee is a decimal, two decimal places are retained, and the excess is discarded.
        # 
        #         - Character: the number of characters.
        #         - DailyActiveUser: the number of daily active users (DAU).
        #         - PeriodMin: the usage duration in minutes (minutes).
        #         - VirtualCpu: the number of virtual CPU cores.
        #         - Unit: the number of units.
        #         - Memory: the memory size (GB).
        #         - KTokens: the number of tokens used (tokens).
        #          Note: The unit of KTokens in the request parameter is tokens, and it does not need to be transformed to thousands of tokens. However, the billing unit is thousands of tokens. Therefore, the token value in the pushed metering parameter is transformed to thousands of tokens during billing. For example, if the pushed usage for 19:00 to 20:00 is 1500 tokens, example: {"Key":"KTokens","Value":"1500","meteringAssit":"cmapi00071246-KTokens-1"}, and the billing price is 1 CNY per thousand tokens, the fee for this period billed hourly is 1500 / 1000 x 1 = 1.5 CNY. If the fee is a decimal, two decimal places are retained, and the excess is discarded.
        #         - Suit: the number of suites. Note that the value passed in the parameter is the number of suites.
        #         - StorageGigaByte: the storage space in GB. Note that the unit of the value directly passed in the parameter is GB, and it does not need to be transformed to bytes or other units.
        #     - Value: the metering value (value >= 0). The parameter type is Integer.
        #     - meteringAssit: instance ID of the multi-dimensional metering item. The parameter type is String. You can view this billing item ID in the product publish backend. Billing items such as Frequency have this value whether there is one or more. When pushing metering data for newly published products, you must pass this parameter.
        #     - SerialNo: specific to large model invoke scenarios. When it is an HTTP invoke, the Settings is requestId. When it is a WebSocket invoke, the Settings is the UID of a single node. This parameter needs to be passed only when the product is billed by the minute. It is not required in other cases.
        # 
        # **Note**:
        # - The multi-dimensional metering capability allows multiple billing items such as Frequency (times), Period (usage duration), and PeriodMin to be configured when publishing a product. For example, a product can have multiple PeriodMin billing items, and each PeriodMin billing item generates a unique ID as the identity of the billing item. This billing item is generated when the product is published, and the format is such as (cmapi00060317-PeriodMin-3, cmapi00060317-PeriodMin-4). When pushing metering data, you need to pass the above ID to perform the corresponding billing deduction. The format of the metering data pushed for newly published products is as follows:
        self.metering = metering

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metering is not None:
            result['Metering'] = self.metering

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metering') is not None:
            self.metering = m.get('Metering')

        return self

