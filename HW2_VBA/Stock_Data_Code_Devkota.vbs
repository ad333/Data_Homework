Option Explicit

Sub stock_market()
    
    '  Define worksheet object
    Dim ws As Worksheet
    
    '  Loop through each worksheet
    For Each ws In Worksheets
        ws.Activate
    
    '  Define array size and counter variables
    Dim size As Long
    Dim i As Long
    
    '  Define ticker symbol and other variables to perform calculations
    Dim ticker_symbol As String
    Dim yearly_open, yearly_close, yearly_change As Double
    Dim percent_yearly_change As Double
    
    '  Initialize variable for holding total stock volume
    Dim total_stock_volume As Double
    total_stock_volume = 0
    
    '  Initialize variable to keep track of location for each ticker symbol in the summary table
    Dim summary_table_row As Long
    summary_table_row = 2
    
        ' Assign labels
        Range("I1").Value = "Ticker"
        Range("J1").Value = "Yearly Change"
        Range("K1").Value = "Percent Change"
        Range("L1").Value = "Total Stock Volume"
        Range("O2").Value = "Greatest % increase"
        Range("O3").Value = "Greatest % Decrease"
        Range("O4").Value = "Greatest Total Volume"
        Range("P1").Value = "Ticker"
        Range("Q1").Value = "Value"
        
        ' Initialize stock open value
        yearly_open = Cells(2, 3).Value
        
        '  Determine the size of count of all stocks
        size = WorksheetFunction.CountA(Range("A:A"))
    
        '  Loop through all stocks
        For i = 2 To size
            
            '  Check if the ticker symbols are different
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                
                '  Set ticker symbol
                ticker_symbol = Cells(i, 1).Value
                
                '  Set yearly close
                yearly_close = Cells(i, 6).Value
                
                '  Calculate yearly change
                yearly_change = yearly_close - yearly_open
                
                '  Calculate percent yearly change
                If yearly_open = 0 Then
                    percent_yearly_change = 0
                Else
                    percent_yearly_change = (yearly_change / yearly_open)
                  
                End If
                
                '  Add to total stock volume
                total_stock_volume = total_stock_volume + Cells(i, 7).Value
            
                '  Print ticker symbol in the summary table
                Range("I" & summary_table_row).Value = ticker_symbol
            
                '  Print yearly change in the summary table
                Range("J" & summary_table_row).Value = yearly_change
            
                '  Print percent yearly change in the summary table
                Range("K" & summary_table_row).Value = percent_yearly_change
                
                '  Format percent yearly change values in the summary table
                Range("K" & summary_table_row).NumberFormat = "0.00%"
            
                '  Print total_stock_volume in the summary table
                Range("L" & summary_table_row).Value = total_stock_volume
            
                '  Increament summary table row
                summary_table_row = summary_table_row + 1
            
                '  Reset the total stock volume
                total_stock_volume = 0
                
                '  Update yearly open price
                yearly_open = Cells(i + 1, 3).Value
            
            '  Else update the total stock volume
            Else
                total_stock_volume = total_stock_volume + Cells(i, 7).Value
           
            End If
       
        Next i

        '  Calculate greatest % increase value and assign to new table
        Range("Q2").Value = Application.WorksheetFunction.Max(Range("K:K"))
        
        '  Calculate greatest % decrease value and assign to new table
        Range("Q3").Value = Application.WorksheetFunction.Min(Range("K:K"))
        
        '  Format percent values
        Range("Q2:Q3").NumberFormat = "0.00%"
        
        '  Calculate greatest total volume and assign to new table
        Range("Q4").Value = Application.WorksheetFunction.Max(Range("L:L"))
        
        '  Define array size and counter variable for summary table
        Dim size1 As Long
        Dim j As Long
        
        '  Determine size of summary table
        size1 = WorksheetFunction.CountA(Range("K:K"))
        
        '  Find ticker symbol corresponding to greatest % increase and print in new table
        For j = 2 To size1
            If Cells(j, 11).Value = Range("Q2").Value Then
                Range("P2").Value = Cells(j, 9).Value
            End If
        Next j
         
        '  Find ticker symbol corresponding to greatest % decrease and print in new table
        For j = 2 To size1
            If Cells(j, 11).Value = Range("Q3").Value Then
                Range("P3").Value = Cells(j, 9).Value
            End If
        Next j
        
        '  Find ticker symbol corresponding to greatest total volume and print in new table
        For j = 2 To size1
           If Cells(j, 12).Value = Range("Q4").Value Then
                Range("P4").Value = Cells(j, 9).Value
           End If
        Next j
        
        '  Conditional formatting to highlight positive change to green and negative change to red
        For j = 2 To size1
           If Cells(j, 11).Value > 0 Then
               Cells(j, 11).Interior.Color = vbGreen
           ElseIf Cells(j, 11).Value < 0 Then
               Cells(j, 11).Interior.Color = vbRed
           End If
        Next j
       
        '  Format column width to fit all columns
        Range("A:Q").EntireColumn.AutoFit
        
    '  Go to next worksheet
    Next ws
   
End Sub
          
            
