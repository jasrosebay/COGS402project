$(document).ready(function() {

    console.log("ready");

// VARIABLES

    var keys = [];
    var employeeCount = 0;
    // var userID = "";
    var companyHrs = {};
    var userID;
    var employeeName;
    var employeeTotalHrs;
    var iCount = 0;
    var jCount = 0;
    var totalEmployeeCount = 0;
    var companyList = [];
    var companyTotalHours = [];
    var grandTotal = [];
    var companiesNum = companyList.length;
    var fields= [];

    $("#btn1").click(function(e) {
        console.log("button 1 clicked");
    });

    $("#display").click(function(e) {
        console.log("display button clicked");
        var x = $('#year').val();
        console.log("x: " + x)
        fetch();
    });

var monthInSummaryPage = "";
var yearInSummaryPage = "";
var clientInSummaryPage = "";
var serviceInSummaryPage = "";

    $("#filterSummary").click(function(e) {

        $('#currentFilter').empty();

        console.log("filterSummary button clicked");
        monthInSummaryPage = $('#monthInSummaryPage').val();
        console.log("monthInSummaryPage: " + monthInSummaryPage)

        // var monthWordInSummaryPage = $('#monthInSummaryPage').val().text();
        // var monthWordInSummaryPage = monthInSummaryPage;

        $('#currentFilter').append("MONTH #: " + monthInSummaryPage + "</br>"); 

        yearInSummaryPage = $('#yearInSummaryPage').val();
        console.log("yearInSummaryPage: " + yearInSummaryPage)

        $('#currentFilter').append("YEAR: " + yearInSummaryPage + "</br>"); 

        clientInSummaryPage = $('#clientInSummaryPage').val();
        console.log("clientInSummaryPage: " + clientInSummaryPage)

        $('#currentFilter').append("CLIENT: " + clientInSummaryPage + "</br>"); 

        // serviceInSummaryPage = $('#serviceInSummaryPage').val();
        // console.log("serviceInSummaryPage: " + serviceInSummaryPage)

        // $('#currentFilter').append("SERVICE: " + serviceInSummaryPage + "</br>"); 

        filteredSummarizeHours(clientInSummaryPage);
       
        // fetch();
    });
 summarizeHours();
function getFields(){
    $.ajax({
            url: '/getFields',
            data: $('form').serialize(),
            type: 'GET',
            success: function(data) {
            	// console.log(data)
				
				for (let i = 0 ; i < data.length; i++) {
					fields.push(data[i]);
				}

				// console.log("____________Fields: ")
				// for (let i = 0 ; i < fields.length; i++) {
				// 	console.log(fields[i]);
				// }
            	// console.log("totalEmployeeCount = " + data);
            	// totalEmployeeCount = parseInt(data)
            },
            error: function(error) {
                console.log(error);
            }
    });
}

getFields();

var employees = [];

function getEmployees(){
    $.ajax({
            url: '/getEmployees',
            data: $('form').serialize(),
            type: 'GET',
            success: function(data) {
                // console.log(data)
                
                for (let i = 0 ; i < data.length; i++) {
                    employees.push(data[i]);
                }

                // console.log("____________Employees: ")
                for (let i = 0 ; i < fields.length; i++) {
                    // console.log(employees[i]);
                    $('select[name=usernameInSummaryPage]').append(
                        $('<option>', {
                            value: employees[i],
                            text: employees[i]
                        })
                    );
                    $('select[name=usernameInSummaryPage]').append('</option>');

                }
                // console.log("totalEmployeeCount = " + data);
                // totalEmployeeCount = parseInt(data)
            },
            error: function(error) {
                console.log(error);
            }
    });
}

getEmployees();

var clientList = [];

function getClients(){
    $.ajax({
            url: '/getClients',
            data: $('form').serialize(),
            type: 'GET',
            success: function(data) {
                // console.log(data)
                
                for (let i = 0 ; i < data.length; i++) {
                    clientList.push(data[i]);
                }

                // console.log("____________Clients: ")
                for (let i = 0 ; i < clientList.length; i++) {
                    // console.log(clientList[i]);
                    $('select[name=clientInSummaryPage]').append(
                        $('<option>', {
                            value: clientList[i],
                            text: clientList[i]
                        })
                    );
                    $('select[name=clientInSummaryPage]').append('</option>');

                }
            },
            error: function(error) {
                console.log(error);
            }
    });
}

getClients();

var serviceList = [];

function getServiceItems(){
    $.ajax({
            url: '/getServiceItems',
            data: $('form').serialize(),
            type: 'GET',
            success: function(data) {
                // console.log(data)
                
                for (let i = 0 ; i < data.length; i++) {
                    serviceList.push(data[i]);
                }

                // console.log("____________Services: ")
                for (let i = 0 ; i < serviceList.length; i++) {
                    // console.log(serviceList[i]);
                    $('select[name=serviceInSummaryPage]').append(
                        $('<option>', {
                            value: serviceList[i],
                            text: serviceList[i]
                        })
                    );
                    $('select[name=serviceInSummaryPage]').append('</option>');

                }
            },
            error: function(error) {
                console.log(error);
            }
    });
}

getServiceItems();


var headers = ["Employee", "First Name", "Last Name", "Date", "Hours", "Client", "Service"]

function fetch(){
        // e.preventDefault()
        $.ajax({
            url: '/getdata',
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                $( "#tsheetsData" ).empty();

                var objLength = 0

                $( "#tsheetsData" ).append('<table class="w3-table-all w3-hoverable"');

                for (i in headers){
                    $( "#tsheetsData" ).append("<th>" + headers[i] + "</th>");
                }

                
                $( "#tsheetsData" ).append('<tbody id="myTable">');

                for (row of Object.entries(response)) {
                    console.log(row[1]);
                    
                    $( "#tsheetsData" ).append("<tr>");

                    var fieldIndex = 0
                    
                    for (value of row[1]){

                        var currentField = fields[fieldIndex];
                        var currentValueOfField = value;
                        
                        console.log("fieldIndex: " + fieldIndex)
                        // if ((fieldIndex == 0) && (fieldIndex == 1) && (fieldIndex == 2) && (fieldIndex == 6) && (fieldIndex == 12) && (fieldIndex == 16)){
                        if ((fieldIndex == 0) | (fieldIndex == 2) | (fieldIndex == 3) | (fieldIndex == 6) |  (fieldIndex == 11) | (fieldIndex == 12) | (fieldIndex == 16)){
                            $( "#tsheetsData" ).append("<td>" + currentValueOfField + "</td");
                        }

                        // console.log(currentField + ": " + currentValueOfField);
                        // $( "#tsheetsData" ).append(currentField + ": " + currentValueOfField + ", ");
                        // $( "#tsheetsData" ).append("<p>" + currentField + ": " + currentValueOfField + "</p>");
                        // console.log(fields[fieldIndex] + ": " + j)
                        fieldIndex += 1;
                    }
                    $( "#tsheetsData" ).append("</tr>");

                    
                    objLength += 1;
                }
                console.log("# of items: ")
                console.log(objLength); 
                $( "#tsheetsData" ).append('/<tbody>');


                $( "#tsheetsData" ).append("</table>");

                // console.log(Object.keys(response)); //index
                // console.log(Object.keys(response[0][15]));

                // for (i of Object.entries(response)) {
                //  console.log(Object.keys(i));
                //  console.log(Object.values(i));
                // }
                // setTimeout(fetchall,1000);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

// fetch();

summaryHeaders = ["Client", "Service", "Total # of Hours for given Date Range"]

headersForEmployeeHrsSummaryPerClientService = ["Employee", "# of Hours"]

function summarizeHours(){
        // e.preventDefault()
        $.ajax({
            url: '/summarizehours',
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                // console.log(response);
                // alert("summarize");

                $( "#summaryTsheetsData" ).empty();

                prevclientService = ""
                iCount = 0
                var totalHoursPerClientPerEmployee = 0

                for (item of Object.entries(response)) {
                    // console.log("item: " + item);
                    // console.log("item[0]: " + item[0]);
                    // console.log("item[1]: " + item[1]);
                    clientService = item[1][0];
                    // console.log("item[1][0] companyService: " + clientService);
                    client = clientService[0];
                    service = clientService[1];
                    // console.log("client: " + client);
                    // console.log("service: " + service);
                    employee = item[1][1];
                    hours = item[1][2];
                    // console.log("employee: " + employee);
                    // console.log("hours: " + hours);

                    // console.log("prevclientService: " + prevclientService);
                    // console.log(prevclientService.toString() != clientService.toString());
                            // totalHoursPerClientPerEmployee = 0;

// var clientInSummaryPage = "";
// var serviceInSummaryPage = "";
                //     console.log("clientInSummaryPage: " + clientInSummaryPage);
                //     console.log("client: " + client);
                //     var x = clientInSummaryPage == client;
                // console.log("_________clientInSummaryPage == client: " + x)
                // console.log("_________serviceInSummaryPage == service: " + serviceInSummaryPage == service)
            // if(x){
                    if (prevclientService.toString() != clientService.toString()){

                        if (totalHoursPerClientPerEmployee > 0){
                            $( "#summaryTsheetsData" ).append("<tr id='totalOFTableData'>" + "<td>Total</td> <td> " + totalHoursPerClientPerEmployee.toFixed(2) + "</td></tr> </br>");
                        }

                        // $( "#summaryTsheetsData" ).append("<div style='background-color: yellow !important;''>");

                        $( "#summaryTsheetsData" ).append("</br></br><h3> " + client + " - " + service + "</h3>");

                        $( "#summaryTsheetsData" ).append('<table class="w3-table-all w3-hoverable"');
                        $( "#summaryTsheetsData" ).append('<tbody id="myTable">');
                        $( "#summaryTsheetsData" ).append("<tr>");
                        for (i in headersForEmployeeHrsSummaryPerClientService){
                            $( "#summaryTsheetsData" ).append("<th>" + headersForEmployeeHrsSummaryPerClientService[i] + "</th>");
                        }

                        $( "#summaryTsheetsData" ).append("</tr>");
                        $( "#summaryTsheetsData" ).append('</tbody>');

                        // $( "#summaryTsheetsData" ).append("CLIENT: " + client + " - " + service + "</br>");
                        totalHoursPerClientPerEmployee = 0;
                            // $( "#summaryTsheetsData" ).append("</br>");

                    }
                    else{

                            $( "#summaryTsheetsData" ).append("</table>");
                            // $( "#summaryTsheetsData" ).append("</br>");
                                                    // $( "#summaryTsheetsData" ).append("</div>");

                    }
                    // $( "#summaryTsheetsData" ).append("<tr>" + "<td>" + employee + "</td>" ": " + hours + "</tr>");
                    totalHoursPerClientPerEmployee += hours;    
                    $( "#summaryTsheetsData" ).append("<tr>" + "<td>" + employee + "</td> <td> " + hours + "</td></tr>");

                    // $( "#summaryTsheetsData" ).append("<tr>" + "<td>" + employee + "</td> <td> " + hours + "</td></tr>");
                        // $( "#summaryTsheetsData" ).append("<tr>" + "<td>Total</td> <td> " + totalHoursPerClientPerEmployee + "</td></tr>");

                    prevclientService = clientService;
                   // } 
// }
                } //for


            },
            error: function(error) {
                console.log(error);
            }
        });
    }


function filteredSummarizeHours(currClient){
        // e.preventDefault()
        $.ajax({
            url: '/summarizehours',
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                // console.log(response);
                // alert("summarize");

                $( "#summaryTsheetsData" ).empty();

                prevclientService = ""
                iCount = 0
                var totalHoursPerClientPerEmployee = 0
                // var currClient =

                for (item of Object.entries(response)) {
                    // console.log("item: " + item);
                    // console.log("item[0]: " + item[0]);
                    // console.log("item[1]: " + item[1]);
                    clientService = item[1][0];
                    // console.log("item[1][0] companyService: " + clientService);
                    client = clientService[0];
                    service = clientService[1];
                    // console.log("client: " + client);
                    // console.log("service: " + service);
                    employee = item[1][1];
                    hours = item[1][2];
                    // console.log("employee: " + employee);
                    // console.log("hours: " + hours);

                    // console.log("prevclientService: " + prevclientService);
                    // console.log(prevclientService.toString() != clientService.toString());
                            // totalHoursPerClientPerEmployee = 0;

// var clientInSummaryPage = "";
// var serviceInSummaryPage = "";
                //     console.log("clientInSummaryPage: " + clientInSummaryPage);
                //     console.log("client: " + client);
                //     var x = clientInSummaryPage == client;
                // console.log("_________clientInSummaryPage == client: " + x)
                // console.log("_________serviceInSummaryPage == service: " + serviceInSummaryPage == service)
            // if(x){

var resultCount = 0;                
if(currClient == client){ 
    // resultCount += 1;

                    // if ((prevclientService.toString() != clientService.toString())){

// if(totalHoursPerClientPerEmployee > 0 & (prevclientService.toString() == clientService.toString()) ){
//                             $( "#summaryTsheetsData" ).append("<tr id='totalOFTableData'>" + "<td>Total</td> <td> " + totalHoursPerClientPerEmployee.toFixed(2) + "</td></tr> </br>");
// }

                    if (prevclientService.toString() != clientService.toString()){

if(totalHoursPerClientPerEmployee > 0){
                            $( "#summaryTsheetsData" ).append("<tr id='totalOFTableData'>" + "<td>Total</td> <td> " + totalHoursPerClientPerEmployee.toFixed(2) + "</td></tr> </br>");
}
                        // $( "#summaryTsheetsData" ).append("<div style='background-color: yellow !important;''>");

                        $( "#summaryTsheetsData" ).append("</br></br><h3> " + client + " - " + service + "</h3>");

                        $( "#summaryTsheetsData" ).append('<table class="w3-table-all w3-hoverable"');
                        $( "#summaryTsheetsData" ).append('<tbody id="myTable">');
                        $( "#summaryTsheetsData" ).append("<tr>");
                        for (i in headersForEmployeeHrsSummaryPerClientService){
                            $( "#summaryTsheetsData" ).append("<th>" + headersForEmployeeHrsSummaryPerClientService[i] + "</th>");
                        }

                        $( "#summaryTsheetsData" ).append("</tr>");
                        $( "#summaryTsheetsData" ).append('</tbody>');

                        // $( "#summaryTsheetsData" ).append("CLIENT: " + client + " - " + service + "</br>");

                        totalHoursPerClientPerEmployee = 0;
                            // $( "#summaryTsheetsData" ).append("</br>");

                    }
                            // $( "#summaryTsheetsData" ).append("<tr id='totalOFTableData'>" + "<td>Total</td> <td> " + totalHoursPerClientPerEmployee.toFixed(2) + "</td></tr> </br>");

                    // $( "#summaryTsheetsData" ).append("<tr>" + "<td>" + employee + "</td>" ": " + hours + "</tr>");
                    totalHoursPerClientPerEmployee += hours;    
                    $( "#summaryTsheetsData" ).append("<tr>" + "<td>" + employee + "</td> <td> " + hours + "</td></tr>");
                            // $( "#summaryTsheetsData" ).append("<tr id='totalOFTableData'>" + "<td>Total</td> <td> " + totalHoursPerClientPerEmployee.toFixed(2) + "</td></tr> </br>");
                        // if (totalHoursPerClientPerEmployee > 0){
                        //     $( "#summaryTsheetsData" ).append("<tr id='totalOFTableData'>" + "<td>Total</td> <td> " + totalHoursPerClientPerEmployee.toFixed(2) + "</td></tr> </br>");
                        // }

                    // $( "#summaryTsheetsData" ).append("<tr>" + "<td>" + employee + "</td> <td> " + hours + "</td></tr>");
                        // $( "#summaryTsheetsData" ).append("<tr>" + "<td>Total</td> <td> " + totalHoursPerClientPerEmployee + "</td></tr>");

                    prevclientService = clientService;
                   // } 
// }
}
                            // $( "#summaryTsheetsData" ).append("<tr id='totalOFTableData'>" + "<td>Total</td> <td> " + totalHoursPerClientPerEmployee.toFixed(2) + "</td></tr> </br>");

                } //for
                        $( "#summaryTsheetsData" ).append('</table>');


            },
            error: function(error) {
                console.log(error);
            }
        });
    }

});