from pyscript import display

band = {'Kelsey', 'Selena', 'Juanico', 'Phoebe', 'Anduin'}
dance = {'Jennifer', 'Sasha', 'Ella', 'Jade', 'Erich', 'Juanico'}

display(band | dance, target='output')
display(band & dance, target='output')
display(band - dance, target='output')
display(dance - band, target='output')
display(band ^ dance, target='output')  