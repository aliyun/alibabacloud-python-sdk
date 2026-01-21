# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricTopRequest(DaraModel):
    def __init__(
        self,
        dimensions: str = None,
        end_time: str = None,
        express: str = None,
        length: str = None,
        metric_name: str = None,
        namespace: str = None,
        order_desc: str = None,
        orderby: str = None,
        period: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The monitoring dimensions of the specified resource.
        # 
        # Set the value to a collection of `key:value` pairs. Example: `{"userId":"120886317861****"}` or `{"instanceId":"i-2ze2d6j5uhg20x47****"}`.
        # 
        # >  You can query a maximum of 50 instances in each request.
        self.dimensions = dimensions
        # The end of the time range to query monitoring data.
        # 
        # *   If the `StartTime` and `EndTime` parameters are not specified, the monitoring data of the last statistical period is queried.``
        # 
        # *   If the `StartTime` and `EndTime` parameters are specified, the monitoring data of the last statistical period in the specified time range is queried.````
        # 
        #     *   If you set the `Period` parameter to 15, the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021-05-08 08:10:00 and the EndTime parameter to 2021-05-08 08:30:00, the monitoring data of the last 15 seconds in the time range is queried.
        #     *   If you set the `Period` parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021-05-08 08:00:00, and the EndTime parameter to 2021-05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried.
        #     *   If you set the `Period` parameter to 3600, the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021-05-08 08:00:00 and the EndTime parameter to 2021-05-10 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried.
        # 
        # The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970
        # *   Time format: YYYY-MM-DDThh:mm:ssZ
        # 
        # >  We recommend that you use UNIX timestamps to prevent time zone-related issues.
        self.end_time = end_time
        # The expression that is used to compute the query results in real time.
        # 
        # >  Only the `groupby` expression is supported. This expression is similar to the GROUP BY statement used in databases.
        self.express = express
        # The number of entries per page.
        # 
        # Default value: 10.
        # 
        # >  The maximum value of the Length parameter in a request is 1440.
        self.length = length
        # The metric that is used to monitor the cloud service.
        # 
        # For more information about metric names, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # For more information about the namespaces of cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The order in which data is sorted. Valid values:
        # 
        # *   True: sorts data in ascending order.
        # *   False (default): sorts data in descending order.
        self.order_desc = order_desc
        # The field based on which data is sorted. Valid values:
        # 
        # *   Average
        # *   Minimum
        # *   Maximum
        # 
        # This parameter is required.
        self.orderby = orderby
        # The statistical period of the monitoring data.
        # 
        # Valid values: 15, 60, 900, and 3600.
        # 
        # Unit: seconds.
        # 
        # > 
        # 
        # *   If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported.
        # 
        # *   Statistical periods vary based on the metrics that are specified by `MetricName`. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.period = period
        self.region_id = region_id
        # The start of the time range to query monitoring data.
        # 
        # *   If the `StartTime` and `EndTime` parameters are not specified, the monitoring data of the last statistical period is queried.``
        # 
        # *   If the `StartTime` and `EndTime` parameters are specified, the monitoring data of the last statistical period in the specified time range is queried.````
        # 
        #     *   If you set the `Period` parameter to 15, the specified time range must be less than or equal to 20 minutes. For example, if you set the StartTime parameter to 2021-05-08 08:10:00 and the EndTime parameter to 2021-05-08 08:30:00, the monitoring data of the last 15 seconds in the time range is queried.
        #     *   If you set the `Period` parameter to 60 or 900, the specified time range must be less than or equal to 2 hours. For example, if you set the Period parameter to 60, the StartTime parameter to 2021-05-08 08:00:00, and the EndTime parameter to 2021-05-08 10:00:00, the monitoring data of the last 60 seconds in the time range is queried.
        #     *   If you set the `Period` parameter to 3600, the specified time range must be less than or equal to two days. For example, if you set the StartTime parameter to 2021-05-08 08:00:00 and the EndTime parameter to 2021-05-10 08:00:00, the monitoring data of the last 3,600 seconds in the time range is queried.
        # 
        # The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 Thursday, January 1, 1970
        # *   Time format: YYYY-MM-DDThh:mm:ssZ
        # 
        # > 
        # 
        # *   You must set the `StartTime` parameter to a point in time that is later than 00:00:00 Thursday, January 1, 1970. Otherwise, this parameter is invalid.
        # 
        # *   We recommend that you use UNIX timestamps to prevent time zone-related issues.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.express is not None:
            result['Express'] = self.express

        if self.length is not None:
            result['Length'] = self.length

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.order_desc is not None:
            result['OrderDesc'] = self.order_desc

        if self.orderby is not None:
            result['Orderby'] = self.orderby

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Express') is not None:
            self.express = m.get('Express')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('OrderDesc') is not None:
            self.order_desc = m.get('OrderDesc')

        if m.get('Orderby') is not None:
            self.orderby = m.get('Orderby')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

