# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceMonitorDataResponseBody(DaraModel):
    def __init__(
        self,
        monitor_data: main_models.DescribeInstanceMonitorDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        # The monitoring data of the instance.
        self.monitor_data = monitor_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorData') is not None:
            temp_model = main_models.DescribeInstanceMonitorDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m.get('MonitorData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceMonitorDataResponseBodyMonitorData(DaraModel):
    def __init__(
        self,
        instance_monitor_data: List[main_models.DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData] = None,
    ):
        self.instance_monitor_data = instance_monitor_data

    def validate(self):
        if self.instance_monitor_data:
            for v1 in self.instance_monitor_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceMonitorData'] = []
        if self.instance_monitor_data is not None:
            for k1 in self.instance_monitor_data:
                result['InstanceMonitorData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_monitor_data = []
        if m.get('InstanceMonitorData') is not None:
            for k1 in m.get('InstanceMonitorData'):
                temp_model = main_models.DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData()
                self.instance_monitor_data.append(temp_model.from_map(k1))

        return self

class DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData(DaraModel):
    def __init__(
        self,
        bpsread: int = None,
        bpswrite: int = None,
        cpu: int = None,
        cpuadvance_credit_balance: float = None,
        cpucredit_balance: float = None,
        cpucredit_usage: float = None,
        cpunotpaid_surplus_credit_usage: float = None,
        iopsread: int = None,
        iopswrite: int = None,
        instance_id: str = None,
        internet_bandwidth: int = None,
        internet_rx: int = None,
        internet_tx: int = None,
        intranet_bandwidth: int = None,
        intranet_rx: int = None,
        intranet_tx: int = None,
        time_stamp: str = None,
    ):
        # The read bandwidth of the cloud disks (system disk and data disks). Unit: Byte/s.
        self.bpsread = bpsread
        # The write bandwidth of the cloud disks (system disk and data disks). Unit: Byte/s.
        self.bpswrite = bpswrite
        # The vCPU utilization of the instance. Unit: percent (%).
        self.cpu = cpu
        # The overdrawn CPU credits of the burstable instance.
        self.cpuadvance_credit_balance = cpuadvance_credit_balance
        # The total number of CPU credits of the burstable instance.
        self.cpucredit_balance = cpucredit_balance
        # The number of CPU credits consumed by the burstable instance.
        self.cpucredit_usage = cpucredit_usage
        # The unpaid overdrawn CPU credits.
        self.cpunotpaid_surplus_credit_usage = cpunotpaid_surplus_credit_usage
        # The number of read I/O operations per second on the cloud disks (system disk and data disks).
        self.iopsread = iopsread
        # The number of write I/O operations per second on the cloud disks (system disk and data disks).
        self.iopswrite = iopswrite
        # The instance ID.
        self.instance_id = instance_id
        # The public bandwidth of the instance. Unit: Kbit/s.
        self.internet_bandwidth = internet_bandwidth
        # The Internet traffic received by the instance during the period that is specified by the `Period` parameter. The period starts from the point in time that is specified by the `TimeStamp` parameter. Unit: Kbit.
        self.internet_rx = internet_rx
        # The Internet traffic sent by the instance during the period that is specified by the `Period` parameter. The period starts from the point in time that is specified by the `TimeStamp` parameter. Unit: Kbit.
        self.internet_tx = internet_tx
        # The internal bandwidth of the instance. Unit: Kbit/s.
        self.intranet_bandwidth = intranet_bandwidth
        # The internal data traffic received by the instance during the period that is specified by the `Period` parameter. The period starts from the point in time that is specified by the `TimeStamp` parameter. Unit: Kbit.
        self.intranet_rx = intranet_rx
        # The internal data traffic sent by the instance during the period that is specified by the `Period` parameter. The period starts from the point in time that is specified by the `TimeStamp` parameter. Unit: Kbit.
        self.intranet_tx = intranet_tx
        # The timestamp of the monitoring data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bpsread is not None:
            result['BPSRead'] = self.bpsread

        if self.bpswrite is not None:
            result['BPSWrite'] = self.bpswrite

        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.cpuadvance_credit_balance is not None:
            result['CPUAdvanceCreditBalance'] = self.cpuadvance_credit_balance

        if self.cpucredit_balance is not None:
            result['CPUCreditBalance'] = self.cpucredit_balance

        if self.cpucredit_usage is not None:
            result['CPUCreditUsage'] = self.cpucredit_usage

        if self.cpunotpaid_surplus_credit_usage is not None:
            result['CPUNotpaidSurplusCreditUsage'] = self.cpunotpaid_surplus_credit_usage

        if self.iopsread is not None:
            result['IOPSRead'] = self.iopsread

        if self.iopswrite is not None:
            result['IOPSWrite'] = self.iopswrite

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_bandwidth is not None:
            result['InternetBandwidth'] = self.internet_bandwidth

        if self.internet_rx is not None:
            result['InternetRX'] = self.internet_rx

        if self.internet_tx is not None:
            result['InternetTX'] = self.internet_tx

        if self.intranet_bandwidth is not None:
            result['IntranetBandwidth'] = self.intranet_bandwidth

        if self.intranet_rx is not None:
            result['IntranetRX'] = self.intranet_rx

        if self.intranet_tx is not None:
            result['IntranetTX'] = self.intranet_tx

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BPSRead') is not None:
            self.bpsread = m.get('BPSRead')

        if m.get('BPSWrite') is not None:
            self.bpswrite = m.get('BPSWrite')

        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('CPUAdvanceCreditBalance') is not None:
            self.cpuadvance_credit_balance = m.get('CPUAdvanceCreditBalance')

        if m.get('CPUCreditBalance') is not None:
            self.cpucredit_balance = m.get('CPUCreditBalance')

        if m.get('CPUCreditUsage') is not None:
            self.cpucredit_usage = m.get('CPUCreditUsage')

        if m.get('CPUNotpaidSurplusCreditUsage') is not None:
            self.cpunotpaid_surplus_credit_usage = m.get('CPUNotpaidSurplusCreditUsage')

        if m.get('IOPSRead') is not None:
            self.iopsread = m.get('IOPSRead')

        if m.get('IOPSWrite') is not None:
            self.iopswrite = m.get('IOPSWrite')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetBandwidth') is not None:
            self.internet_bandwidth = m.get('InternetBandwidth')

        if m.get('InternetRX') is not None:
            self.internet_rx = m.get('InternetRX')

        if m.get('InternetTX') is not None:
            self.internet_tx = m.get('InternetTX')

        if m.get('IntranetBandwidth') is not None:
            self.intranet_bandwidth = m.get('IntranetBandwidth')

        if m.get('IntranetRX') is not None:
            self.intranet_rx = m.get('IntranetRX')

        if m.get('IntranetTX') is not None:
            self.intranet_tx = m.get('IntranetTX')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

