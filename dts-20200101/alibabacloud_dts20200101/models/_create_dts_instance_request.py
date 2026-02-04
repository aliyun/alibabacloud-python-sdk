# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDtsInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_start: bool = None,
        compute_unit: int = None,
        database_count: int = None,
        destination_endpoint_engine_name: str = None,
        destination_region: str = None,
        dts_region: str = None,
        du: int = None,
        fee_type: str = None,
        insight_module: bool = None,
        instance_class: str = None,
        job_id: str = None,
        max_du: float = None,
        min_du: float = None,
        pay_type: str = None,
        period: str = None,
        quantity: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_endpoint_engine_name: str = None,
        source_region: str = None,
        sync_architecture: str = None,
        type: str = None,
        used_time: int = None,
    ):
        # Specifies whether to automatically renew the DTS instance when it expires. Valid values:
        # 
        # *   **false**: does not automatically renew the DTS instance when it expires. This is the default value.
        # *   **true**: automatically renews the DTS instance when it expires.
        self.auto_pay = auto_pay
        # Specifies whether to automatically start the task after the DTS instance is purchased. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        # 
        # >  This parameter can be set to **true** and take effect only if you specify a valid value for **JobId**.
        self.auto_start = auto_start
        # The specification of the extract, transform, and load (ETL) instance. The unit is compute unit (CU). One CU is equal to 1 vCPU and 4 GB of memory. The value of this parameter must be an integer greater than or equal to 2.
        self.compute_unit = compute_unit
        # The number of custom ApsaraDB RDS instances in the PolarDB-X instance. Default value: **1**.
        # 
        # >  This parameter is required only if **SourceEndpointEngineName** is set to **drds**.
        self.database_count = database_count
        # The database engine of the destination instance.
        # 
        # *   **MySQL**: ApsaraDB RDS for MySQL instance or self-managed MySQL database
        # *   **PolarDB**: PolarDB for MySQL cluster
        # *   **polardb_o**: PolarDB for Oracle cluster
        # *   **polardb_pg**: PolarDB for PostgreSQL cluster
        # *   **Redis**: ApsaraDB for Redis instance or self-managed Redis database
        # *   **DRDS**: PolarDB-X 1.0 or PolarDB-X 2.0 instance
        # *   **PostgreSQL**: self-managed PostgreSQL database
        # *   **odps**: MaxCompute project
        # *   **oracle**: self-managed Oracle database
        # *   **mongodb**: ApsaraDB for MongoDB instance or self-managed MongoDB database
        # *   **tidb**: TiDB database
        # *   **ADS**: AnalyticDB for MySQL V2.0 cluster
        # *   **ADB30**: AnalyticDB for MySQL V3.0 cluster
        # *   **Greenplum**: AnalyticDB for PostgreSQL instance
        # *   **MSSQL**: ApsaraDB RDS for SQL Server instance or self-managed SQL Server database
        # *   **kafka**: Message Queue for Apache Kafka instance or self-managed Kafka cluster
        # *   **DataHub**: DataHub project
        # *   **DB2**: self-managed Db2 for LUW database
        # *   **as400**: AS/400
        # *   **Tablestore**: Tablestore instance
        # 
        # > 
        # *   The default value is **MySQL**.
        # *   For more information about the supported source and destination databases, see [Overview of data synchronization scenarios](https://help.aliyun.com/document_detail/130744.html) and [Overview of data migration scenarios](https://help.aliyun.com/document_detail/26618.html).
        # *   You must specify one of this parameter and the **JobId** parameter.
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        # The ID of the region in which the destination instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # >  You must specify one of this parameter and the **JobId** parameter.
        self.destination_region = destination_region
        # The region ID of the DTS instance. Set this parameter to the value of **RegionId**.
        self.dts_region = dts_region
        # The number of DTS units (DUs) that are assigned to a DTS task that is run on a DTS dedicated cluster. Valid values: **1** to **100**.
        # 
        # > 
        # *   The value of this parameter must be within the range of the number of DUs available for the DTS dedicated cluster.
        self.du = du
        # The billing type for a change tracking instance. Valid values: ONLY_CONFIGURATION_FEE and CONFIGURATION_FEE_AND_DATA_FEE. ONLY_CONFIGURATION_FEE: charges only configuration fees. CONFIGURATION_FEE_AND_DATA_FEE: charges configuration fees and data traffic fees.
        self.fee_type = fee_type
        self.insight_module = insight_module
        # The instance class.
        # 
        # *   DTS supports the following instance classes for a data migration instance: **xxlarge**, **xlarge**, **large**, **medium**, and **small**.
        # *   DTS supports the following instance classes for a data synchronization instance: **large**, **medium**, **small**, and **micro**.
        # 
        # >  For more information about the test performance of each instance class, see [Specifications of data migration instances](https://help.aliyun.com/document_detail/26606.html) and [Specifications of data synchronization instances](https://help.aliyun.com/document_detail/26605.html).
        self.instance_class = instance_class
        # The ID of the task. You can call the **ConfigureDtsJob** operation to obtain the task ID from the **DtsJobId** parameter.
        # 
        # >  If this parameter is specified, you do not need to specify the **SourceRegion**, **DestinationRegion**, **Type**, **SourceEndpointEngineName**, or **DestinationEndpointEngineName** parameter. Even if these parameters are specified, the value of the **JobId** parameter takes precedence.
        self.job_id = job_id
        # Upper limit of DU.
        # 
        # > Only supported by Serverless instances.
        self.max_du = max_du
        # Lower limit of DU.
        # 
        # > Only supported by Serverless instances.
        self.min_du = min_du
        # The billing method. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        # 
        # >  This parameter must be specified.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values: **Year** and **Month**.
        # 
        # >  You must specify this parameter only if the **PayType** parameter is set to **PrePaid**.
        self.period = period
        # The number of DTS instances that you want to purchase.
        # 
        # >  You can purchase only one DTS instance each time you call this operation.
        self.quantity = quantity
        # The ID of the region in which the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The database engine of the source instance.
        # 
        # *   **MySQL**: ApsaraDB RDS for MySQL instance or self-managed MySQL database
        # *   **PolarDB**: PolarDB for MySQL cluster
        # *   **polardb_o**: PolarDB for Oracle cluster
        # *   **polardb_pg**: PolarDB for PostgreSQL cluster
        # *   **Redis**: ApsaraDB for Redis instance or self-managed Redis database
        # *   **DRDS**: PolarDB-X 1.0 or PolarDB-X 2.0 instance
        # *   **PostgreSQL**: self-managed PostgreSQL database
        # *   **odps**: MaxCompute project
        # *   **oracle**: self-managed Oracle database
        # *   **mongodb**: ApsaraDB for MongoDB instance or self-managed MongoDB database
        # *   **tidb**: TiDB database
        # *   **ADS**: AnalyticDB for MySQL V2.0 cluster
        # *   **ADB30**: AnalyticDB for MySQL V3.0 cluster
        # *   **Greenplum**: AnalyticDB for PostgreSQL instance
        # *   **MSSQL**: ApsaraDB RDS for SQL Server instance or self-managed SQL Server database
        # *   **kafka**: Message Queue for Apache Kafka instance or self-managed Kafka cluster
        # *   **DataHub**: DataHub project
        # *   **DB2**: self-managed Db2 for LUW database
        # *   **as400**: AS/400
        # *   **Tablestore**: Tablestore instance
        # 
        # > 
        # *   The default value is **MySQL**.
        # *   For more information about the supported source and destination databases, see [Overview of data synchronization scenarios](https://help.aliyun.com/document_detail/130744.html) and [Overview of data migration scenarios](https://help.aliyun.com/document_detail/26618.html).
        # *   You must specify one of this parameter and the **JobId** parameter.
        self.source_endpoint_engine_name = source_endpoint_engine_name
        # The ID of the region in which the source instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # >  You must specify one of this parameter and the **JobId** parameter.
        self.source_region = source_region
        # The synchronization topology. Valid values:
        # 
        # *   **oneway**: one-way synchronization. This is the default value.
        # *   **bidirectional**: two-way synchronization.
        self.sync_architecture = sync_architecture
        # The type of the DTS instance. Valid values:
        # 
        # *   **MIGRATION**: data migration instance
        # 
        # *   **SYNC**: data synchronization instance
        # 
        # *   **SUBSCRIBE**: change tracking instance
        # 
        # > You must specify one of this parameter and the **JobId** parameter.
        self.type = type
        # The subscription duration.
        # 
        # *   Valid values if **Period** is set to **Month**: 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        # *   Valid values if **Period** is set to **Year**: 1, 2, 3, and 5.
        # 
        # > 
        # 
        # *   This parameter is valid and required only if **PayType** is set to **PrePaid**.
        # 
        # *   You can configure **Period** to specify the unit of the subscription duration.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start

        if self.compute_unit is not None:
            result['ComputeUnit'] = self.compute_unit

        if self.database_count is not None:
            result['DatabaseCount'] = self.database_count

        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name

        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region

        if self.dts_region is not None:
            result['DtsRegion'] = self.dts_region

        if self.du is not None:
            result['Du'] = self.du

        if self.fee_type is not None:
            result['FeeType'] = self.fee_type

        if self.insight_module is not None:
            result['InsightModule'] = self.insight_module

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.max_du is not None:
            result['MaxDu'] = self.max_du

        if self.min_du is not None:
            result['MinDu'] = self.min_du

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.sync_architecture is not None:
            result['SyncArchitecture'] = self.sync_architecture

        if self.type is not None:
            result['Type'] = self.type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')

        if m.get('ComputeUnit') is not None:
            self.compute_unit = m.get('ComputeUnit')

        if m.get('DatabaseCount') is not None:
            self.database_count = m.get('DatabaseCount')

        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')

        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')

        if m.get('DtsRegion') is not None:
            self.dts_region = m.get('DtsRegion')

        if m.get('Du') is not None:
            self.du = m.get('Du')

        if m.get('FeeType') is not None:
            self.fee_type = m.get('FeeType')

        if m.get('InsightModule') is not None:
            self.insight_module = m.get('InsightModule')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MaxDu') is not None:
            self.max_du = m.get('MaxDu')

        if m.get('MinDu') is not None:
            self.min_du = m.get('MinDu')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SyncArchitecture') is not None:
            self.sync_architecture = m.get('SyncArchitecture')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

