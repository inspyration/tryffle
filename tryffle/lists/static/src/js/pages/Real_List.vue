<script setup lang="ts">
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net';
import 'datatables.net-buttons';
import 'datatables.net-buttons/js/buttons.html5';
import 'datatables.net-responsive';
import 'datatables.net-select';
import 'datatables.net-select';

DataTable.use(DataTablesCore);

const columns = [
  { data: 'document_name' },
  { data: 'page_number' },
  { data: 'text' },
];

const options = {
  dom: 'Bftip',
  responsive: true,
  select: true,
};
</script>

<template>
  <div style="text-align: center; max-width: 1200px;">
    <h1>Ajax data source table</h1>
    <h2>DataTables + Vue3 example</h2>
    <p>
      In this example the <code>datatables.net-vue3</code> package is used to
      load JSON data and display it in an interactive table. In this case we use
      object based row data, rather than arrays, so the
      <code>columns</code> option is specified to tell DataTables which property
      to read from the objects for each column.
    </p>
    <p>
      This example demonstrates how DataTables' extensions can be used with
      Vue3. The key is to import and then register them with the
      <code>DataTable.use()</code> method. They can then be used as a regular
      DataTable extension. In this example I demonstrate Select and Buttons
      being loaded in.
    </p>

    <DataTable
      :columns="columns"
      :options="options"
      ajax='/seb/data/'
      class="display nowrap"
      width="100%"
    >
      <thead>
        <tr>
          <th>Document Name</th>
          <th>Page number</th>
          <th>Text</th>
        </tr>
      </thead>
      <tfoot>
        <tr>
          <th>Document Name</th>
          <th>Page number</th>
          <th>Text</th>
        </tr>
      </tfoot>
    </DataTable>
  </div>
</template>

<style>
@import 'datatables.net-dt';
@import 'datatables.net-buttons-dt';
@import 'datatables.net-responsive-dt';
@import 'datatables.net-select-dt';
</style>
